
# Leetcode 152: https://leetcode.com/problems/maximum-score-after-splitting-a-string/
# Pattern: Prefix Sum 


class Solution:
    def maxScore(self, s: str) -> int:

        maxSum = 0 
        leftZeros = 0
        rightOnes = s.count('1')

        for i in range(len(s)-1):
            if s[i] == '0':
                leftZeros += 1
            else:
                rightOnes -= 1

            maxSum = max(maxSum, leftZeros + rightOnes )
        return maxSum

    # Time Complexity: O(n)
    # Space Complexity: O(1)








         # Brute Force Approach

# class Solution:
#     def maxScore(self, s: str) -> int:

#         n = len(s)
#         maxSum = 0 
#         for i in range(1, n):
#             left = s[:i]
#             right = s[i:]
#             leftZeros = left.count('0')
#             rightOnes = right.count('1')

#             maxSum = max(maxSum, leftZeros + rightOnes )
#         return maxSum

    # Time Complexity: O(n^2)
    # Space Complexity: O(n)