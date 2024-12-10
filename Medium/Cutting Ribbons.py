'''
https://leetcode.com/problems/cutting-ribbons

After seeing hints
Binary search with bounds from 1 to max(ribbons)
For each search, pick a value X, and check if we can get K ribbons of length X.
To do so, do a greedy one-pass approach. Take as many Xs from each ribbon until
either reaching the end or taking K Xs.

TC: O(N log max(ribbons))
SC: O(1)
'''
class Solution:
    # Optimized version
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_get_k_ribbons(x):
            count = 0
            for ribbon in ribbons:
                count += ribbon // x
                if count >= k:
                    # Early return if we've already found k ribbons
                    return True
            return False
        
        # Binary search to maximize X
        lo = 1
        hi = max(ribbons)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if can_get_k_ribbons(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
      
'''
Test cases
[8, 8, 8]
k = 3
=> 8

[8, 8, 8]
k = 6
=> 4

[8, 8, 8]
k = 1
=> 8

[8, 8, 8]
k = 12
=> 2
'''
