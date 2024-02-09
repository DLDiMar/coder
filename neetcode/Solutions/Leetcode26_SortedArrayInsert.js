// Leetcode 26: Remove Duplicates from Sorted Array
// Ascending order array, need to keep same-size array but remove duplicates

// Method: traverse array and shift unique values over duplicate values as encountered.

// Input starter code

var assert = require('assert');

var removeDuplicates = function(nums) {
    // Initiate pointers for indexes
    let [left, right] = [0, 0];

    while (right < nums.length) {
        // Initiate values at pointers
        const [leftVal, rightVal] = [nums[left], nums[right]];
        const isEqual = (rightVal === leftVal);
        
        // If values at pointers aren't equal, move left pointer up and shift values to left.
        // End while loop with condition to move right pointer.
        if (!isEqual) {
            left++;
            nums[left] = rightVal;
        }

        right++;
    }

    return (left + 1);
};

let nums = [1,1,2,2,3,4,5,5,6,7,7,8]; // Input array
let expectedNums = [1,2,3,4,5,6,7,8,6,7,7,8]; // The expected answer with correct length

let k = removeDuplicates(nums); // Calls your implementation

console.log("Expected Array: " + expectedNums);
console.log("Actual Array: " + nums);
