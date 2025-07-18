
# Leetcode 2574: https://leetcode.com/problems/left-and-right-sum-differences/
# Pattern: Prefix Sum 


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum  = [0] * n
        rightSum  = [0] * n
        outputArray = [0] * n
        for i in range(1,len(nums)):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            outputArray[i] = abs(leftSum[i] - rightSum[i])
        return outputArray
            
# Time Complexity: O(n)
# Space Complexity: O(n)
    