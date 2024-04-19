/*
Intuition:
- We use a two-pointer approach to iterate through both lists of intervals simultaneously.
- At each iteration, we check for overlaps between intervals and calculate the intersection if there is any.
- We move pointers based on which interval ends earlier, ensuring that we efficiently cover all possible intersections.

Time Complexity: O(m + n)
- 'm' and 'n' represent the lengths of the firstList and secondList, respectively.
- We iterate through both lists simultaneously, processing each interval once.
- Hence, the time complexity is linear with respect to the total number of intervals in both lists.

Space Complexity: O(min(m, n))
- We use a list to store the intersections found, which could have a maximum size of min(m, n) if all intervals intersect.
- Therefore, the space complexity is proportional to the smaller of the two input lists.
*/
public class Solution {
    public int[][] IntervalIntersection(int[][] firstList, int[][] secondList) {
        // Initialize a list to store the intersections found
        List<int[]> intersections = new List<int[]>();
        
        // Initialize pointers for both lists
        int i = 0, j = 0;
        
        // Iterate through both lists simultaneously until one of the lists is fully processed
        while (i < firstList.Length && j < secondList.Length) {
            // Retrieve start and end points of intervals from both lists
            int startA = firstList[i][0];
            int endA = firstList[i][1];
            int startB = secondList[j][0];
            int endB = secondList[j][1];
            
            // Check if there is an overlap between the intervals
            if (endA >= startB && endB >= startA) {
                // Calculate the intersection start and end points
                int intersectionStart = Math.Max(startA, startB);
                int intersectionEnd = Math.Min(endA, endB);
                
                // Add the intersection to the list of intersections
                intersections.Add(new int[] { intersectionStart, intersectionEnd });
            }
            
            // Move pointers to the next intervals based on which one ends earlier
            if (endA < endB) {
                i++;
            } else {
                j++;
            }
        }
        
        // Convert the list of intersections to a 2D array and return
        return intersections.ToArray();
    }
}
