

# Leetcode 3194:   https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements
# Pattern: Two Pointer Appproch 

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums.sort()
        i = 0
        j = len(nums) -1
        # min_avg to positive infinity, which ensures that any average value you compute will be smaller
        min_avg = float('inf')

        while i < j:
            avg = (nums[i] + nums[j])/2
            min_avg = min(min_avg, avg)
            i += 1;
            j -= 1;
        return min_avg

             
    # Time Complexity: O(nlogn)  log n for sorting
    # Space Complexity: O(1)


