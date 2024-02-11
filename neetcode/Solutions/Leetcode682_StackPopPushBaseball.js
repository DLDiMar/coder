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