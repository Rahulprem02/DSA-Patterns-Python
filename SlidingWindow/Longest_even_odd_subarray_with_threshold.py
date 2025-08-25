
# Leetcode 2760: https://leetcode.com/problems/longest-even-odd-subarray-with-threshold
# Pattern: Sliding Window (Dynamic)


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        maxLen = 0
        n = len(nums)
        length = 0

        for i in range(n):
    # Check if nums[i] can be a valid start
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                length = 1   # starting subarray has length 1
                j = i
                while j + 1 < n and nums[j+1] <= threshold and (nums[j] % 2 != nums[j+1] % 2):
                    length += 1
                    j += 1
            maxLen = max(maxLen, length)
        return maxLen

    # ChatGPT logic
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
        