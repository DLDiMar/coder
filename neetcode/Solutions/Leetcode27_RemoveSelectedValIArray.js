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