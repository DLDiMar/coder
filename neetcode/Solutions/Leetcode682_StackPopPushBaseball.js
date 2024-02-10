/**
 * @param {string[]} operations
 * @return {number}
 */

var sumArray = function (array) {
    let sum = 0;
    return array.forEach(x => {
        sum += x;
    });
}

var calPoints = function(operations) {
    // sum at the very end whole array
    // get a running variable return of an int
    // Want O(1) operations each time for push, pop, and peek
    // Total O(2n) ( aka O(n) )target speed, since have to pop n times for sum
    let record = new Array(operations.length);
    let sum = 0;
    
    if (operations.length = 0) { return 0; }
    
    // traverse operations array and do what it needs to do
    // if ops[i] is D, take ops value and insert 2*value
    // if ops[i] is C, pop last record out
    // if ops[i] is +, add last value + 2nd last value of record
    // else, push onto the record array
    for (let i = 0; i < operations.length; i++) {
        if (operations[i] === "D") {
            record.push(operations[i] * 2);
        }
        if (operations[i] === "C") {
            record.pop();
        }
        if (operations[i] === "+") {
            record.push(record[record.length-1] + record[record.length-2]);
        }
        else {
            record.push(operations[i]);
        }
    }
    return sumArray(record);
};