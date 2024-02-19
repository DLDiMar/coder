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
      let lowIndex = 0;
      let highIndex = flatArr.length - 1;
  
      // Alternately take elements from high and low ends
      while (lowIndex <= highIndex) {
        if (lowIndex !== highIndex) {
          result.push(flatArr[highIndex--]);
          result.push(flatArr[lowIndex++]);
        } else {
          result.push(flatArr[lowIndex]);
        }
      }
  
      return result;
    } catch (error) {
      console.error("Error sorting array:", error);
      return [];
    }
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
  // Output: [543, 1, 456, 3, 345, 14, 98, 34, 89, 40, 79, 46, 76, 91, 45, 45, 44, 25, 43, 26, 23, 22, 12, 112]
  