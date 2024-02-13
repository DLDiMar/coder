/* 
Time Complexity: O(n)
The algorithm uses two pointers, left and right, and iterates through the array once with the while loop.
The loop condition while (right < nums.length) ensures that each element is processed once.
The operations inside the loop (comparisons, updates) are constant time.
Therefore, the overall time complexity is linear, O(n), where n is the length of the input array.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space regardless of the size of the input array.
The extra space is used for the pointers left and right, as well as a few constant variables (leftVal, rightVal, isEqual).
The space complexity is independent of the input size, making it O(1).
*/

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
