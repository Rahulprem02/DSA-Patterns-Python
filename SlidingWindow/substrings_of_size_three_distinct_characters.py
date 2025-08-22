
# Leetcode 1876: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters
# Pattern: Sliding Window (Fixed)

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s) - 2):  # stop at len(s)-3
            substring = s[i:i+3]     # take substring of length 3
            if len(set(substring)) == 3:
                count += 1
        return count

   # Time Complexity: O(n)
   # Space Complexity: O(1)  