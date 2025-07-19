

# Leetcode 1664: https://leetcode.com/problems/ways-to-make-a-fair-array/
# Pattern: Prefix Sum 


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        prefixEven = [0] * (len(nums) + 1)
        prefixOdd = [0] * (len(nums) + 1)
        count = 0

        for i in range(len(nums)):
            prefixEven[i+1] = prefixEven[i]
            prefixOdd[i+1] = prefixOdd[i]
            if i%2==0:
                prefixEven[i+1] += nums[i]
            else:
                prefixOdd[i+1] += nums[i]
        for i in range(len(nums)):
            even_sum = prefixEven[i] + (prefixOdd[len(nums)] - prefixOdd[i+1])
            odd_sum = prefixOdd[i] + (prefixEven[len(nums)] - prefixEven[i+1])
            
            if even_sum == odd_sum:
                count += 1

        return count
        

            # Time Complexity: O(n)
            # Space Complexity: O(n)




        # Brute Force Approach

        # count = 0

        # for i in range(len(nums)):
        #     array = nums[:]  
        #     evenSum = 0
        #     oddSum = 0
        #     array.pop(i)
        #     for j in range(len(array)):
        #         if j%2==0:
        #             evenSum += array[j]
        #         else:
        #             oddSum  +=array[j]
        #     if evenSum == oddSum:
        #         count += 1
        # return count
                    
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    # Error: Time Limit Exceeded
