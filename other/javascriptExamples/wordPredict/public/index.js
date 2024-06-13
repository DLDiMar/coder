const input = document.getElementById('input');
const suggestionsContainer = document.getElementById('suggestions');

input.addEventListener('input', async () => {
  const inputValue = input.value;
  const response = await fetch(`/suggestions?input=${inputValue}`);
  const suggestions = await response.json();
  const suggestionsHtml = suggestions.map((suggestion) => {
    return `<li>${suggestion.word}</li>`;
  }).join('');
  suggestionsContainer.innerHTML = `<ul>${suggestionsHtml}</ul>`;
});