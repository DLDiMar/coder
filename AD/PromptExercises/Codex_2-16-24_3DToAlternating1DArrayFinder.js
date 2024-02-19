function sort3DArrayAlternating(arr) {
  // Handle null or empty input
  if (!arr || arr.length === 0) {
    return [];
  }

  try {
    // Flatten the 3D array into a 1D array
    const flatArr = arr.flat(2);

    // Sort the flattened array in descending order
    flatArr.sort((a, b) => b - a);

    // Initialize variables for alternating output
    const result = [];

    // First push the highest value to result
    result.push(flatArr.shift());

    // Alternately take elements from low and high ends
    while (flatArr.length > 0) {
      if (flatArr.length > 0) {
        result.push(flatArr.pop());
      }
      if (flatArr.length > 0) {
        result.push(flatArr.shift());
      }
    }

    return result;
  } catch (error) {
    console.error("Error sorting array:", error);
    return [];
  }
}

function findValueApprox(sortedArray, targetValue) {
  // Handle edge cases
  if (sortedArray.length === 0) {
    return -1; // Array is empty
  }

  let currentPos = 0;

  while (currentPos < sortedArray.length && targetValue <= sortedArray[currentPos]) {
    if (sortedArray[currentPos] === targetValue) {
      return currentPos; // Return the index where the value is found
    }

    // Proportional jump to the next expected location
    const difference = targetValue + sortedArray[currentPos];
    const jump = Math.max(1, Math.floor(difference / 2));

    // Move to the next expected location
    currentPos += jump;
  }

  return -1; // Value not found
}

const array = [
  [
    [1, 4, 6, 12, 345, 43, 89],
    [23, 45, 456, 98, 22],
    [1, 3]
  ],
  [
    [12, 44, 76, 112, 45, 543, 79],
    [26, 40, 46, 91, 25],
    [14, 34]
  ]
];

const sorted = sort3DArrayAlternating(array);
console.log(sorted);

const finder = findValueApprox(sorted, 45);
console.log(finder);

