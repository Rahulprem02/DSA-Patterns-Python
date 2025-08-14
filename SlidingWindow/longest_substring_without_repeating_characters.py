
# Leetcode 3: hhttps://leetcode.com/problems/longest-substring-without-repeating-characters/
# Pattern: Sliding Window (Dynamic)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)