let parenthesisLibrary = {
    ")" : "(",
    "}" : "{",
    "]" : "["
};

var isValid = function(s) {
    let stack = [];

    for (let char of s) {
        if (char in parenthesisLibrary) {
            let topElement = stack.length === 0 ? 'x' : stack.pop();
            if (parenthesisLibrary[char] !== topElement) {
                return false;
            }
        } else {
            stack.push(char);
        }
    }

    return stack.length === 0;
};

// Example usage:
console.log("Tested string: (). Output: " + isValid("()")); // true
console.log("Tested string: ()[]{}. Output: " + isValid("()[]{}")); // true
console.log("Tested string: (]. Output: " + isValid("(]")); // false
console.log("Tested string: ([)]. Output: " + isValid("([)]")); // false
console.log("Tested string: {[]}. Output: " + isValid("{[]}")); // true
console.log("Tested string: }{. Output: " + isValid("}{")); // false
