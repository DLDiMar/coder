/*
Intuition:
- We aim to find the median of the combined sorted arrays nums1 and nums2 without actually merging the arrays.
- We perform a binary search on the smaller array (nums1) to partition it into two parts such that the elements on the left side are smaller than or equal to the elements on the right side.
- We then calculate the corresponding partition for the larger array (nums2) to ensure that the combined left and right parts contain an equal number of elements.
- We determine the maximum element on the left side (maxLeftX and maxLeftY) and the minimum element on the right side (minRightX and minRightY) for both arrays.
- If the maxLeftX is less than or equal to minRightY and maxLeftY is less than or equal to minRightX, we have found the correct partition. If the combined length of the arrays is even, the median is the average of the maximum element on the left and the minimum element on the right. If the length is odd, the median is the maximum of the two maximum elements on the left.
- If maxLeftX is greater than minRightY, we move the partition towards the left side of nums1. If maxLeftY is greater than minRightX, we move the partition towards the right side of nums1.
- We repeat this process until we find the correct partition.

Time Complexity: O(log(min(x, y))), where x is the length of nums1 and y is the length of nums2. We perform binary search on the smaller array nums1.

Space Complexity: O(1), as we only use a constant amount of extra space for variables.
*/

public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        // Ensure nums1 is smaller or equal in size to nums2
        if (nums1.Length > nums2.Length) {
            return FindMedianSortedArrays(nums2, nums1);
        }

        // Get lengths of both arrays
        int x = nums1.Length;
        int y = nums2.Length;
        int low = 0;
        int high = x;

        // Perform binary search on nums1
        while (low <= high) {
            // Partition nums1
            int partitionX = (low + high) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;

            // Calculate maxLeft and minRight for both arrays
            int maxLeftX = (partitionX == 0) ? int.MinValue : nums1[partitionX - 1];
            int minRightX = (partitionX == x) ? int.MaxValue : nums1[partitionX];
            int maxLeftY = (partitionY == 0) ? int.MinValue : nums2[partitionY - 1];
            int minRightY = (partitionY == y) ? int.MaxValue : nums2[partitionY];

            // Check if partition is correct
            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                // Calculate median based on even or odd total length
                if ((x + y) % 2 == 0) {
                    return (Math.Max(maxLeftX, maxLeftY) + Math.Min(minRightX, minRightY)) / 2.0;
                } else {
                    return Math.Max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) {
                // Adjust partition to left side
                high = partitionX - 1;
            } else {
                // Adjust partition to right side
                low = partitionX + 1;
            }
        }

        // Error case if not found
        throw new Exception("Should not reach here");
    }
}
