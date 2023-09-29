# https://leetcode.com/problems/sqrtx

# 14 ms, beats 83.44%
# 13.06 MB, beats 94.48%

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(math.floor(math.sqrt(x)))
