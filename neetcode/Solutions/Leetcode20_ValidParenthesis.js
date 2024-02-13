/* 
Time Complexity: O(n)
The algorithm iterates through each character in the input string exactly once in the for...of loop.
Each operation inside the loop (pushing and popping from the stack, 
    checking if a character is in parenthesisLibrary, comparing characters) takes constant time.
Therefore, the overall time complexity is linear, O(n), where n is the length of the input string.

Space Complexity: O(n)
The space complexity is determined by the space used by the stack.
In the worst case, all characters from the input string are pushed onto the stack 
(for example, if the input is all opening parentheses). 
Therefore, the space complexity is proportional to the length of the input string, O(n).
*/

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
