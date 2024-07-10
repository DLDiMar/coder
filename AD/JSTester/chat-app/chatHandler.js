import atob from 'atob';
import btoa from 'btoa';
import guid from 'guid';
import miniLock from './utils/miniLock.js';
import { nowUTC } from './utils/time.js';
import { extractMessageMetadata } from './utils/chat.js';
import { Subject, from, of, throwError, Observable, fromEvent } from 'rxjs';
import { ajax } from 'rxjs/ajax';
import { mergeMap, map, mapTo, catchError, tap } from 'rxjs/operators';
import WebSocket from 'ws';

class ChatHandler {
  constructor(wsUrl) {
    this.wsUrl = wsUrl;
    this.wsMessageSubject = null;
    this.wsUserStatusSubject = null;
  }

  onWsClose = (event) => {
    console.error('Websocket got close event', event);
    this.wsMessageSubject.error(new Error('The websocket connection was closed!'));
  }

  onWsError = (event) => {
    console.error('Websocket got error event', event);
    this.wsMessageSubject.error(new Error('Error occurred on websocket connection!'));
  }

  onWsMessage = (event) => {
    let data;
    try {
      data = JSON.parse(event.data);
    } catch (e) {
      console.error('Received non-JSON message', event.data);
      return;
    }

    if (data && data.ephemeral && data.ephemeral.length && data.ephemeral.length > 0) {
      from(data.ephemeral)
        .pipe(
          mergeMap(ephemeral =>
            this.createDecryptEphemeralObservable({ ephemeral, mID: this.mID, secretKey: this.secretKey })),
          mergeMap(this.resolveIncomingMessageTypeObservable),
          catchError(error => {
            console.error('An error occurred in ChatHandler', error);
            return throwError(error);
          })
        )
        .subscribe();
    }
    if (data && data.from_server) {
      if (data.from_server.all_messages_deleted) {
        alert("All messages deleted from server! (Refresh this page to remove them from this browser tab.)");
      }
    }
  }

  resolveIncomingMessageTypeObservable = (message) => {
    if (message.meta.isChatMessage) {
      const reader = new FileReader();
      const chatMessageObservable =
        fromEvent(reader, 'loadend')
          .pipe(
            map(event => JSON.parse(event.target.result)),
            tap(contents => {
              this.wsMessageSubject.next({
                id: guid.create(),
                fromUsername: message.meta.from,
                maybeSenderId: message.maybeSenderId,
                message: contents.msg
              });
            })
          );

      reader.readAsText(message.fileBlob);

      return chatMessageObservable;
    } else if (message.meta.isUserStatus) {
      return of({
        username: message.meta.from,
        status: message.meta.status,
        created: nowUTC()
      }).pipe(
        tap(status => this.wsUserStatusSubject.next(status))
      );
    } else {
      return throwError(new Error('Unrecognized data with type ' + message.tags.type));
    }
  }

  createDecryptEphemeralObservable = ({ ephemeral, mID, secretKey }) => {
    return new Observable(observer => {
      const binStr = atob(ephemeral);
      const binStrLength = binStr.length;
      const array = new Uint8Array(binStrLength);

      for (let i = 0; i < binStrLength; i++) {
        array[i] = binStr.charCodeAt(i);
      }
      const msg = new Blob([array], { type: 'application/octet-stream' });
      miniLock.crypto.decryptFile(msg, mID, secretKey, (fileBlob, saveName, senderID) => {
        const tags = saveName.split('|||');
        const meta = extractMessageMetadata(tags);

        let maybeSenderId = '';
        if (senderID !== this.mID) {
          maybeSenderId = ' (' + senderID + ')';
        }

        observer.next({ fileBlob, saveName, meta, senderID, maybeSenderId });
      });
    });
  }

  send({ contents = {}, tags, ttl = 0 }) {
    if (!this.ws) {
      throw new Error('WebSocket connection not initialized!');
    }
    if (this.ws.readyState !== WebSocket.OPEN) {
      throw new Error('WebSocket connection is initializing and is not open yet!');
    }

    const saveName = tags.join('|||');
    const fileBlob = new Blob([JSON.stringify(contents)], { type: 'application/json' });
    fileBlob.name = saveName;

    const mID = this.mID;
    const secretKey = this.secretKey;
    miniLock.crypto.encryptFile(fileBlob, saveName, [mID], mID, secretKey, this.sendMessageToServer.bind(this, ttl));
  }

  sendMessage(message, username) {
    const contents = {
      msg: message,
      from: username,
      type: 'chatmessage'
    };
    const tags = ['from:' + username, 'type:chatmessage'];
    this.send({ contents, tags });
  }

  sendUserStatus = (username, status, ttl) => {
    const tags = ['from:' + username, 'type:userstatus', 'status:' + status];
    this.send({ tags, ttl });
  }

  sendDeleteAllMessagesSignalToServer = () => {
    const msgForServer = {
      to_server: {
        delete_all_messages: true
      }
    }
    this.ws.send(JSON.stringify(msgForServer));
  }

  sendMessageToServer = (ttl_secs, fileBlob, saveName, senderMinilockID) => {
    const reader = new FileReader();
    reader.addEventListener("loadend", () => {
      // From https://stackoverflow.com/questions/9267899/arraybuffer-to-base64-encoded-string#comment55137593_11562550
      const b64encMinilockFile = btoa([].reduce.call(
        new Uint8Array(reader.result),
        function (p, c) {
          return p + String.fromCharCode(c);
        }, ''));

      const msgForServer = {
        ephemeral: [b64encMinilockFile]
      };
      if (ttl_secs > 0) {
        msgForServer.to_server = {
          ttl_secs: ttl_secs
        };
      }
      this.ws.send(JSON.stringify(msgForServer));
    });
    reader.readAsArrayBuffer(fileBlob);
  }

  initConnection = ({ mID, secretKey, authToken }) => {
    this.mID = mID;
    this.secretKey = secretKey;
    this.authToken = authToken;
    this.wsMessageSubject = new Subject();
    this.wsUserStatusSubject = new Subject();

    return new Observable(observer => {
      this.ws = new WebSocket(this.wsUrl);
      this.ws.onclose = this.onWsClose;
      this.ws.onerror = this.onWsError;
      this.ws.onmessage = this.onWsMessage;
      this.ws.onopen = (event) => {
        event.target.send(this.authToken);
        observer.next();
        observer.complete();
      };
    });
  }

  cleanUp = () => {
    this.wsMessageSubject.complete();
    this.wsMessageSubject = null;
    this.wsUserStatusSubject.complete();
    this.wsUserStatusSubject = null;
    this.ws.close();
    this.ws = null;
    this.mID = null;
    this.secretKey = null;
    this.authToken = null;
  }

  getMessageSubject = () => {
    return this.wsMessageSubject;
  }

  getUserStatusSubject = () => {
    return this.wsUserStatusSubject;
  }
}

// Initialize and use the ChatHandler
const wsUrl = 'ws://localhost:8080';
const chatHandler = new ChatHandler(wsUrl);

chatHandler.initConnection({
  mID: 'your-mID',
  secretKey: 'your-secret-key',
  authToken: 'your-auth-token'
}).subscribe({
  next: () => {
    console.log('WebSocket connection opened');
    // Send a test message
    chatHandler.sendMessage('Hello World', 'Username');
  },
  error: (err) => console.error('WebSocket error:', err),
  complete: () => console.log('WebSocket connection closed')
});

chatHandler.getMessageSubject().subscribe({
  next: (msg) => console.log('Message received:', msg),
  error: (err) => console.error('Message error:', err),
  complete: () => console.log('Message subject closed')
});

chatHandler.getUserStatusSubject().subscribe({
  next: (status) => console.log('User status:', status),
  error: (err) => console.error('Status error:', err),
  complete: () => console.log('Status subject closed')
});
