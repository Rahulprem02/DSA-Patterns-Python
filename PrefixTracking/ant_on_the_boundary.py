
# Leetcode 3028: https://leetcode.com/problems/ant-on-the-boundary/
# Pattern: Prefix Sum 



class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:

        position = 0
        count = 0
        for num in nums:
            position += num
            if position==0:
                count += 1
        return count
    

# Time Complexity: O(n)
# Space Complexity: O(1)