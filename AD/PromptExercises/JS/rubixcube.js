const inputFaces = ['R', 'O', 'Y', 'G', 'B', 'W'];
const outputArray = [];

for (let i = 0; i < 12; i++) {
  const face = inputFaces[i % 6];
  const above = (i === 0) ? 0 : outputArray[i - 1][0];
  const left = (i % 3 === 0) ? 0 : outputArray[i - 1][2];
  const right = (i % 3 === 2) ? 0 : outputArray[i + 1][0];
  const below = (i === 11) ? 0 : outputArray[i + 1][2];

  outputArray.push([
    above,
    left,
    right,
    below,
    face === 'R' ? 1 : 0,
    face === 'O' ? 2 : 0,
    face === 'Y' ? 3 : 0,
    face === 'G' ? 4 : 0,
    face === 'B' ? 5 : 0,
    face === 'W' ? 6 : 0
  ]);
}

console.log(outputArray);