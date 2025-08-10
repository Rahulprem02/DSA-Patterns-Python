
# Leetcode 977: https://leetcode.com/problems/squares-of-a-sorted-array/
# Pattern: Two Pointer Appproch 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = []
        for num in nums:
            squared.append(num * num)
        
        squared.sort()
        
        return squared


    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
        