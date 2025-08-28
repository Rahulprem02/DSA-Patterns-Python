# Leetcode 2762 : https://leetcode.com/problems/continuous-subarrays/
# Pattern: Sliding Window

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
    
        for i in range(n):
            current_min = nums[i]
            current_max = nums[i]
        
            for j in range(i, n):
                current_min = min(current_min, nums[j])
                current_max = max(current_max, nums[j])
            
                if current_max - current_min > 2:
                    break
                count += 1
            
        return count
    
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)