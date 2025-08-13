
# Leetcode 2460:  https://leetcode.com/problems/apply-operations-to-an-array/
# Pattern: Two Pointer Appproch 

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        zeros = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0


        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zeros += 1
        result.extend([0] * zeros)

        return result


    # Time Complexity: O(n)  
    # Space Complexity: O(n)
    #  This is not two pointer appproch solution.