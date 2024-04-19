/*
Intuition:
- We use a sliding window approach to find the length of the longest substring without repeating characters.
- We maintain a HashSet to keep track of the characters in the current substring.
- We use two pointers, i and j, to define the boundaries of the current substring.
- We iterate through the string, expanding the window by moving the j pointer forward.
- If the character at position j is not in the HashSet, we add it to the set and update the currentMax length if needed.
- If the character at position j is already in the HashSet, we shrink the window by moving the i pointer forward and removing characters from the HashSet until the repeating character is no longer in the substring.
- We repeat this process until the end of the string is reached.

Time Complexity: O(n), where n is the length of the input string s. Both pointers i and j traverse the string once.

Space Complexity: O(min(n, m)), where n is the length of the input string s and m is the size of the character set (in this case, the number of unique characters in the string). The space complexity is limited by the size of the HashSet.
*/

public class Solution {
    public int LengthOfLongestSubstring(string s) {
        // Check for empty or null string
        if (s == null || s == String.Empty)
            return 0;

        // Initialize variables
        HashSet<char> set = new HashSet<char>();
        int currentMax = 0,
            i = 0,
            j = 0;

        // Iterate through the string using two pointers
        while (j < s.Length)
            if (!set.Contains(s[j])) {
                // Expand the window and update currentMax if needed
                set.Add(s[j++]);
                currentMax = Math.Max(currentMax, j - i);
            } else {
                // Shrink the window and remove characters until no repeating characters
                set.Remove(s[i++]);
            }

        return currentMax;
    }
}
