# Leetcode 238: https://leetcode.com/problems/product-of-array-except-self/description/
# Pattern: Prefix Sum 


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:



        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]

        return result


# Time Complexity: O(n)
# Space Complexity: O(n)



        # Brute Force Approach
        '''product_list = []
        pro = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    pro =  pro * nums[j]
            product_list.append(pro)
            pro = 1
       
        return product_list
    '''

        
# Time Complexity: O(n^2)
# Space Complexity: O(n)
