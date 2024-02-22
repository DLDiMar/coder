function invertImage(pixels) {
    return pixels.map(row => row.map(pixel => pixel === 1 ? 0 : pixel === 0 ? 1 : 0));
}

function flipHorizontal(pixels) {
    if (!Array.isArray(pixels)) {
      console.error('Input is not an array');
      return pixels; 
    }
  
    return pixels.map(row => Array.isArray(row) ? row.slice().reverse() : row);
  }

function flipVertical(pixels) {
    const N = pixels.length;
    const flipped = new Array(N);
    for (let i = 0; i < N; i++) {
      flipped[i] = pixels[N - i - 1];
    }
    return flipped;
}

function smallMosaic(input) {
  const N = input.length;
  const M = input[0].length;
  const result = new Array(N * 2).fill(0).map(() => new Array(M * 2).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      result[i][j] = input[i][j];
      result[N - i - 1][j] = input[N - i - 1][j];
      result[i][M - j - 1] = input[i][M - j - 1];
      result[N - i - 1][M - j - 1] = input[N - i - 1][M - j - 1];
    }
  }

  return result;
}


const input = [
    [1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1]
];

const smallMosaicOutput = smallMosaic(input);
smallMosaicOutput.forEach(row => console.log(row.join(' ')));
// Output:
// 1 0 1 0 0 0 0 1 0 1
// 0 0 1 1 1 1 1 1 0 0
// 1 1 0 0 0 0 0 0 1 1
// 1 1 1 1 1 1 1 1 1 1
// 1 1 1 1 1 1 1 1 1 1
// 1 1 0 0 0 0 0 0 1 1
// 0 0 1 1 1 1 1 1 0 0
// 1 0 1 0 0 0 0 1 0 1


