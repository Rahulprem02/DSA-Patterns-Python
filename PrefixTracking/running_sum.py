# Leetcode 1480: https://leetcode.com/problems/running-sum-of-1d-array/
# Pattern: Prefix Sum 

#Input: [1,2,3,4]
#Output: [1,3,6,10]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        num = []
        for i in range(len(nums)):
            sum += nums[i]
            num.append(sum)
        return num


# Space Complexity o(n)
#    We loop through the list once → linear time
# Time Complexity  o(n)
#    We create a new list num of size n to store the result
