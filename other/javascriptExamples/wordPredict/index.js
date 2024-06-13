const PredictiveText = require('./predictive-text');

// Create a new instance of the PredictiveText class
const predictiveText = new PredictiveText();

// Example usage:
predictiveText.addWord('hello');
predictiveText.addWord('world');
predictiveText.addWord('hello');
predictiveText.addWord('again');

console.log(predictiveText.getSuggestions('he')); // Output: [{ word: 'hello', frequency: 2 }]