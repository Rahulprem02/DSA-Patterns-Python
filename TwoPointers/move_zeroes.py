

# Leetcode 283: https://leetcode.com/problems/move-zeroes/
# Pattern: Two Pointer Appproch


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        for right in range (len(nums)):
            if nums[right] != 0:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left +=1

    # Time Complexity: O(n)
    # Space Complexity: O(1)
