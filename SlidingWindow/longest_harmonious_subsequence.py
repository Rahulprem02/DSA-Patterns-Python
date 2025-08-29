
# Leetcode 594 : https://leetcode.com/problems/longest-harmonious-subsequence/
# Pattern: Sliding Window 

from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        longest = 0
        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])
        return longest
        
    # Time Complexity:  O(n)
    # Space Complexity: O(n) 