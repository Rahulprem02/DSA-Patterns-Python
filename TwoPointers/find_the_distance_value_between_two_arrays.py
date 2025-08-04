
# Leetcode 1385:   https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Pattern: Two Pointer Appproch 

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        for i in range(len(arr1)):
            is_valid = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    is_valid = False
                    break
            if is_valid:
                count +=1
        return count


        


        # Time Complexity: O(n * m)
        # Space Complexity: O(1)
    

        # arr1 and arr2 same size (n)	O(n²)
        #arr1 has n elements, arr2 has m	O(n × m)