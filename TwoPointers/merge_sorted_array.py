
# Leetcode 88: https://leetcode.com/problems/merge-sorted-array/
# Pattern: Two Pointer Appproch


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        for i in range(len(nums1)):
            if nums1[i] == 0 and j < len(nums2):
                nums1[i] = nums2[j]
                j += 1
       
        nums1 = nums1.sort()
        

        
    # Time Complexity: O((m+n)log(m+n))   Log for sort
    # Space Complexity: O(1)
    #  This is not two pointer appproch solution.
