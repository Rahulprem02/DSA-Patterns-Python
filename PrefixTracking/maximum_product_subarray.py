

# Leetcode 152: https://leetcode.com/problems/maximum-product-subarray/
# Pattern: Prefix Sum 

class Solution:
     def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]
        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            result = max(result, curr_max)

        return  result
     
    # Time Complexity: O(n)
    # Space Complexity: O(1)



        # Brute Force Approach
        """n = len(nums)
        max_product = nums[0]
        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                max_product = max(max_product, product)
         return  max_product
        
        """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

