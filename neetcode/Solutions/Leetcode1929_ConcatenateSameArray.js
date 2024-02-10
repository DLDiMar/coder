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