# Leetcode 3432: https://leetcode.com/problems/count-partitions-with-even-sum-difference/
# Pattern: Prefix Sum 


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        leftSum = 0
        rightsum = 0
        count = 0
        totalSum = sum(nums)

        for i in range(len(nums)-1):
            leftSum += nums[i]
            rightsum = totalSum - leftSum

            if (leftSum - rightsum)%2 == 0:
                count +=1
            rightsum = 0
        
        return count
    
#Time Complexity: O(n)
#Space Complexity: O(1)