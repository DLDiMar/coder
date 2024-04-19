/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
        next = null;
    }

    public Node(int _val, Node _next) {
        val = _val;
        next = _next;
    }
}
*/

/*
Intuition:
- We need to insert the given value into the sorted circular linked list while maintaining its sorted order.
- We handle different cases based on whether the list is empty or not and whether the insertion point is within the existing list or not.
- If the list is empty, we create a new single circular list with the given value.
- Otherwise, we iterate through the list to find the insertion point based on the sorted order.
- Once we find the insertion point, we insert the new node containing the insertVal and adjust the pointers accordingly.

Time Complexity: O(n), where n is the number of nodes in the circular linked list. In the worst case, we may need to iterate through all nodes to find the insertion point.

Space Complexity: O(1), as we are not using any extra space proportional to the input size.
*/

public class Solution {
    public Node Insert(Node head, int insertVal) {
        if (head == null) {
            // If the list is empty, create a new single circular list with insertVal
            Node newNode = new Node(insertVal);
            newNode.next = newNode; // Point to itself
            return newNode;
        }
        
        // Initialize pointers for traversal
        Node prev = head;
        Node curr = head.next;
        bool toInsert = false; // Flag to track if insertVal has been inserted
        
        // Traverse the circular list to find the insertion point
        do {
            if (prev.val <= insertVal && insertVal <= curr.val) {
                // If insertVal falls between prev and curr nodes, insert it here
                toInsert = true;
            } else if (prev.val > curr.val) {
                // Handle the case where we need to insert insertVal between the smallest and largest values
                if (insertVal >= prev.val || insertVal <= curr.val) {
                    toInsert = true;
                }
            }
            
            if (toInsert) {
                prev.next = new Node(insertVal, curr); // Insert new node
                return head; // Return the original head
            }
            
            prev = curr;
            curr = curr.next;
        } while (prev != head);
        
        // If insertVal has not been inserted yet (e.g., all nodes have the same value)
        prev.next = new Node(insertVal, curr); // Insert new node at the end
        return head; // Return the original head
    }
}
