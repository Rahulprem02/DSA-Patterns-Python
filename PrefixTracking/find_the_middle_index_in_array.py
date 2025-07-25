
# Leetcode 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
# Pattern: Prefix Sum 


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:

        left = 0
        right = sum(nums)

        for i in range (len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


# Time Complexity: O(n)
# Space Complexity: O(1)
    