

# Leetcode 303: https://leetcode.com/problems/range-sum-query-immutable/
# Pattern: Prefix Sum 


class NumArray:
    
    prefixSum = []
    def __init__(self, nums: List[int]):
        
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]

        self.prefixSum = nums
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]

        return self.prefixSum[right] - self.prefixSum[left-1]
        
        

    # Time Complexity: O(n)
    # Space Complexity: O(1)
