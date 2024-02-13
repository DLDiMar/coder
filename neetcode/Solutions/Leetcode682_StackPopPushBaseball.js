/*

Time Complexity: O(n)
The algorithm uses a single for loop to iterate through each operation in the operations array exactly once.
The operations inside the loop are basic arithmetic operations, condition checks, and array manipulations, all of which take constant time.
Therefore, the overall time complexity is linear, O(n), where n is the length of the input operations array.

Space Complexity: O(n)
The space complexity is determined by the size of the record array.
In the worst case, the record array may store all the numerical values from the operations array.
Therefore, the space complexity is proportional to the length of the input operations array, O(n).

*/

// Solve an array by traversing origianl 'operations' array for commands
// Note the push and pop methods available in js for stacks/arrays
// Assume C, D, and + will never start in first array index

var calPoints = function(operations) {
    // declare sume for return
    // declare record array/stack to do operations on
    // For each operation (use for loop):
    //    if op = c, pop the record value from the running sum
    //    if op = d, double the record value at index and push onto record. Don't forget to add to running sum.
    //    if op = +, add two last index values of record, then push onto record. Don't forget to add to the running sum.
    //    Anything else, push onto the record stack and add it to the running sum.
    // Return running sum
    let runningSum = 0;
    const record = [];
    for(const o of operations) {
        if(o === 'C') {
            runningSum -= record.pop();
            continue;
        }
        if(o === 'D') {
            const val = record[record.length - 1] * 2;
            record.push(val);
            runningSum += val;
            continue;
        }
        if(o === '+') {
            const val = record[record.length - 1] + record[record.length - 2];
            record.push(val);
            runningSum += val;
            continue;
        }
        record.push(+o);
        runningSum += +o;
    }
    return runningSum;
};

let operations = ["5","-2","4","C","D","9","+","+"]
let expectedOutput = 27;

let k = calPoints2(operations);

console.log("Expected Value: " + expectedOutput);
console.log("Actual Output: " + k);