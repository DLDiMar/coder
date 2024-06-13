const PredictiveText = require('./predictive-text');

const inputField = document.getElementById('input-field');
const suggestionsDiv = document.getElementById('suggestions');

const predictiveText = new PredictiveText();

inputField.addEventListener('input', (e) => {
  const input = e.target.value;
  const suggestions = predictiveText.getSuggestions(input);
  displaySuggestions(suggestions);
});

function displaySuggestions(suggestions) {
  suggestionsDiv.innerHTML = '';
  suggestions.forEach((suggestion) => {
    const suggestionDiv = document.createElement('div');
    suggestionDiv.textContent = suggestion.word;
    suggestionDiv.className = 'suggestion';
    suggestionsDiv.appendChild(suggestionDiv);
  });
}

// Example usage:
predictiveText.addSentence('Hello world this is a test sentence.');
predictiveText.addSentence('Hello again this is another test sentence.');