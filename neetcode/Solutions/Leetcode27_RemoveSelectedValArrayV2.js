/* 
Time Complexity: O(n)
The algorithm uses two pointers, leftPtr and rightPtr, and iterates through the array once with the while loop.
The loop condition while (leftPtr > -1) ensures that each element is processed once.
Inside the loop, there are constant-time operations, such as comparisons and swaps.
Therefore, the overall time complexity is linear, O(n), where n is the length of the input array.

Space Complexity: O(1)
The algorithm uses a constant amount of extra space regardless of the size of the input array.
The extra space is used for the pointers leftPtr, rightPtr, and a few constant variables (temp).
The space complexity is independent of the input size, making it O(1).
*/

// Remove a specific value inside an array, keeping the same size at least.
// Don't forget edge cases!
// EC1: 0-size array: return 0
// EC1: 1-size array: if only value is val, return 0, otherwise return 1
                                                                                                                
// Method: create 2 pointers, starting at the end
// While left pointer is not past 0 index (-1)
//    If value at right pointer is value, move right pointer to left
//    After that, while left pointer equals value, move both pointers left
//    Otherwise, if left pointer is value, put a temp value of left pointer value
//    Then, switch values where right pointer value is left pointer value, make right pointer value the temp value, and decrease right pointer
// After all that, make sure to move left pointer left. Then, return right pointer position + 1 (arrays start at 0, so total length needs extra 1)

var removeElement = function(nums, val) {
    if (nums.length === 0) { return 0; }
    if (nums.length === 1) {
        if (nums[0] === val) { return 0; }
        else { return 1; }
    }

    let leftPtr = nums.length - 2;
    let rightPtr = nums.length - 1;

    while (leftPtr > -1 ) {
        if (nums[rightPtr] === val) {
            rightPtr--;
            while (nums[leftPtr] === val) {
                rightPtr--;
                leftPtr--;
            }
        }
        else if (nums[leftPtr] === val) {
            let temp = nums[leftPtr];
            nums[leftPtr] = nums[rightPtr];
            nums[rightPtr] = temp;
            leftPtr--;
        }
        leftPtr--;
    }
    return rightPtr + 1;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
}

let nums = [2,7,4,5,2,2,9,8]; // Input array
let val = 2; // Value to remove
let expectedNums = [7,4,5,9,8]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

let k = removeElement(nums, val); // Calls your implementation

console.log("Version 2: Expected Array: " + expectedNums);
console.log("Version 2: Actual Array: " + nums);