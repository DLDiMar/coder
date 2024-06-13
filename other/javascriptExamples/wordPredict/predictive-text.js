class TrieNode {
    constructor() {
      this.children = {};
      this.endOfWord = false;
      this.frequency = 0;
      this.nextWords = {};
    }
  }
  
  class PredictiveText {
    constructor() {
      this.trie = new TrieNode();
      this.context = '';
    }
  
    // Add a word to the trie
    addWord(word) {
      let currentNode = this.trie;
      for (let char of word) {
        if (!currentNode.children[char]) {
          currentNode.children[char] = new TrieNode();
        }
        currentNode = currentNode.children[char];
      }
      currentNode.endOfWord = true;
      currentNode.frequency++;
    }
  
    // Add a sentence to the trie
    addSentence(sentence) {
      const words = sentence.split(' ');
      for (let i = 0; i < words.length; i++) {
        this.addWord(words[i]);
        if (i > 0) {
          this.addNextWord(words[i - 1], words[i]);
        }
      }
    }
  
    // Add a next word to the trie
    addNextWord(context, word) {
      let currentNode = this.trie;
      for (let char of context) {
        if (!currentNode.children[char]) {
          currentNode.children[char] = new TrieNode();
        }
        currentNode = currentNode.children[char];
      }
      if (!currentNode.nextWords[word]) {
        currentNode.nextWords[word] = 0;
      }
      currentNode.nextWords[word]++;
    }
  
    // Get suggestions based on the user's input
    getSuggestions(input) {
      if (input.endsWith('.')) {
        this.context = '';
        return [];
      }
      const words = input.split(' ');
      const lastWord = words[words.length - 1];
      if (words.length > 1) {
        this.context = words[words.length - 2];
      }
      let currentNode = this.trie;
      for (let char of lastWord) {
        if (!currentNode.children[char]) {
          return [];
        }
        currentNode = currentNode.children[char];
      }
      if (this.context) {
        return this._getNextWordSuggestions(currentNode, this.context);
      } else {
        return this._getSuggestionsRecursive(currentNode, lastWord);
      }
    }
  
    // Recursive function to get suggestions
    _getSuggestionsRecursive(node, prefix) {
      let suggestions = [];
      if (node.endOfWord) {
        suggestions.push({ word: prefix, frequency: node.frequency });
      }
      for (let char in node.children) {
        suggestions = suggestions.concat(this._getSuggestionsRecursive(node.children[char], prefix + char));
      }
      return suggestions;
    }
  
    // Get next word suggestions based on the context
    _getNextWordSuggestions(node, context) {
      let suggestions = [];
      for (let word in node.nextWords) {
        suggestions.push({ word: word, frequency: node.nextWords[word] });
      }
      return suggestions;
    }
  }
  
  module.exports = PredictiveText;