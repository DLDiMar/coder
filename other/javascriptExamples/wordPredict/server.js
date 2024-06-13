const express = require('express');
const app = express();
const PredictiveText = require('./predictive-text');

const predictiveText = new PredictiveText();

// Add some sample words to the trie
predictiveText.addNextWord('hello');
predictiveText.addNextWord('world');
predictiveText.addNextWord('hello');
predictiveText.addNextWord('again');

app.use(express.static('public'));

app.get('/suggestions', (req, res) => {
  const input = req.query.input;
  const suggestions = predictiveText.getSuggestions(input);
  res.json(suggestions);
});

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});