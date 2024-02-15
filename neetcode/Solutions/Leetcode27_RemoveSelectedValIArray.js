/*
Time Complexity: O(n^2)
The primary reason for the time complexity is the use of the splice method inside the loop. When splice is called, it may take O(n) time to shift the elements after the removal point to fill the gap.
In each iteration of the loop, if an element is removed using splice, the subsequent shifting of elements may cause the entire array to be traversed multiple times.
Therefore, the overall time complexity is O(n^2), where n is the length of the input array.

Space Complexity: O(1)
The space complexity is constant because the algorithm doesn't use additional data structures that scale with the input size.
However, keep in mind that the splice method modifies the array in place, and it may use extra memory for temporary storage during the element shifting.
Despite this, the space used by splice is not proportional to the input size, so the space complexity is considered O(1).

*/

var removeElement = function(nums, val) {
    let k = 0;
    
    for (let p = 0; p < nums.length; p++) {
        if (nums[p] === val) {
            // splice replaces an element with one next to it if 2nd param = 1
            nums.splice(p, 1);
            p--;
        }
    }
    return nums.length;
};

let nums = [2,7,4,5,2,2,9,8]; // Input array
let val = 2; // Value to remove
let expectedNums = [7,4,5,9,8]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

let k = removeElement(nums, val); // Calls your implementation

console.log("Version 1: Expected Array: " + expectedNums);
console.log("Version 1: Actual Array: " + nums);