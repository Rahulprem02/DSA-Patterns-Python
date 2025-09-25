

# Leetcode 448: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array
# Data Structure: Array 


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums) 
        x = []
        for i in range(1, n + 1):
            if i not in num_set:
                x.append(i)
        return x


 # Time Complexity: O(n)
 # Space Complexity: O(n)
