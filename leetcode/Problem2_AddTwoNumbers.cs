/*
Intuition:
- We traverse both linked lists simultaneously, adding the corresponding node values along with any carry from the previous addition.
- We maintain a dummy head to simplify the code and handle edge cases.
- We iterate until both input lists are exhausted, considering the case where one list is longer than the other.
- At each step, we calculate the sum of the current nodes' values along with the carry, update the carry for the next iteration, and create a new node with the sum's least significant digit.
- Finally, if there's any remaining carry after the iteration, we add a new node to the result list.

Time Complexity: O(max(m, n)), where m and n are the lengths of the input linked lists l1 and l2, respectively. We iterate through at most max(m, n) nodes to calculate the sum.

Space Complexity: O(max(m, n)), the maximum length of the resulting linked list can be at most one node longer than the longer input list, due to the carry.
*/

// public class ListNode {
//     public int val;
//     public ListNode next;
//     public ListNode(int val=0, ListNode next=null) {
//         this.val = val;
//         this.next = next;
//     }
// }

public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        // Initialize a dummy head for the result linked list
        ListNode dummyHead = new ListNode(0);
        // Initialize pointers for the input lists and the result list
        ListNode p = l1, q = l2, curr = dummyHead;
        // Initialize carry for addition
        int carry = 0;
        
        // Iterate through both input lists until both are exhausted
        while (p != null || q != null) {
            // Retrieve the current node values of l1 and l2 (or 0 if null)
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            // Calculate the sum of current node values and carry
            int sum = carry + x + y;
            // Update carry for the next iteration
            carry = sum / 10;
            // Create a new node with the least significant digit of the sum
            curr.next = new ListNode(sum % 10);
            // Move the result list pointer to the newly created node
            curr = curr.next;
            // Move pointers of input lists to the next nodes
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        
        // Check if there's any remaining carry after the iteration
        if (carry > 0) {
            // Add a new node to the result list with the remaining carry
            curr.next = new ListNode(carry);
        }
        
        // Return the result list starting from the node after the dummy head
        return dummyHead.next;
    }
}
