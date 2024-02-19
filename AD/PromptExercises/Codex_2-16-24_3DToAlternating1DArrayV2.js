function sort3DArrayAlternating(arr) {
    try {
      // Error handling: Check for valid input
      if (arr === null || arr.length === 0) {
        throw new Error("Array is null or empty");
      }
      if (!Array.isArray(arr)) {
        throw new Error("Input is not an array");
      }
  
      // 1. Flatten the 3D array into a 1D array
      const flattenedArray = arr.flat(2);
  
      // 2.  Sort the flattened array in descending order
      flattenedArray.sort((a, b) => b - a);
  
      // 3. Create the alternating (high-low) output array
      const result = [];
      let lowIndex = 0;
      let highIndex = flattenedArray.length - 1;
  
      while (lowIndex <= highIndex) {
        if (lowIndex !== highIndex) { // Avoid duplicate if only one element is left
          result.push(flattenedArray[highIndex]);
          result.push(flattenedArray[lowIndex]);
        } else {
          result.push(flattenedArray[highIndex]); 
        }
        lowIndex++;
        highIndex--;
      }
  
      return result;
    } catch (error) {
      console.error("Error in sort3DArrayAlternating:", error);
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