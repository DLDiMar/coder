import WebSocket from 'ws';

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    ws.send(JSON.stringify({ from_server: { all_messages_deleted: true } }));
  });

  ws.send(JSON.stringify({ message: 'something' }));
});

console.log('WebSocket server is running on ws://localhost:8080');
