# Leetcode 3090: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Pattern: Sliding Window (Dynamic)


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        counts = {}

        for right in range(len(s)):
            if s[right] in counts:
                counts[s[right]] += 1
            else:
                counts[s[right]] = 1

            while counts[s[right]] > 2:
                counts[s[left]] -= 1  # remove char at left
                left += 1

            maxLen = max(maxLen, right - left + 1)
        return maxLen
    
     # Time Complexity: O(n)
   # Space Complexity: O(1)  