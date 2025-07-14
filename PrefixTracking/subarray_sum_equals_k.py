
# 560. Subarray Sum Equals K

# Leetcode 560: https://leetcode.com/problems/subarray-sum-equals-k/
# Pattern: Prefix Sum 


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    
        prefix_sum =0 
        countN = 0

        hash_map = {0: 1}  

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in hash_map:
                countN += hash_map[prefix_sum - k]
            
            hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
        
        return countN
    
    # Time Complexity: O(n)
    # We loop through the list once, doing constant-time operations each step.

    # Space Complexity: O(n)
    # We use a hashmap to store prefix sums, which can hold up to n entries in the worst case.

    
    # Brute Force Approach
    ''' count = 0
        for i in range(len(nums)):
            sum = 0 
            for j in range( i ,len(nums)):
                sum += nums[j]
                if sum == k:
                    count = count + 1
        
        return count
    '''

# Time Complexity: O(n^2)
# Two nested loops to consider all subarrays.

# Space Complexity: O(1)
# Only a few variables used, no extra data structures proportional to input size.

