
# Leetcode 724: https://leetcode.com/problems/find-pivot-index /
# Pattern: Prefix Sum 


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        leftSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1

# Time Complexity: O(n)
# Space Complexity: O(1)