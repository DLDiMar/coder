/*

Time Complexity: O(n)
The algorithm uses a single for loop to iterate through each index in the ans array, where n is the length of the input array nums.
Inside the loop, the operations (insertions and assignments) are constant time.
Therefore, the overall time complexity is linear, O(n), where n is the length of the input array nums.

Space Complexity: O(n)
The space complexity is determined by the size of the ans array.
The ans array is allocated with a size of 2n, where n is the length of the input array nums.
Therefore, the space complexity is proportional to the length of the input array nums, O(n).

*/


// Concatnates the same array to a new array twice
// allocated the new array of size 2n 
// The first half is direct insert
// Then, second half is inserted at index - old array length

var getConcatenation = function(nums) {
    let newLength = nums.length * 2;
    let ans = new Array(newLength);
    
    for (let i = 0; i < newLength; i++) {
        if (i < nums.length) {
            ans[i] = nums[i];
        }
        if (i >= nums.length) {
            ans[i] = ans[i-nums.length];
        }
    }
    return ans;
};

let nums = [1,3,7,3,4];
let expectedAns = [1,3,7,3,4,1,3,7,3,4];

let k = getConcatenation(nums);

console.log("Expected Array: " + expectedAns);
console.log("Actual Array: " + k);