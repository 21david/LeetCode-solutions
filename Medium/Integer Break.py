# https://leetcode.com/problems/integer-break/

class Solution(object):
    def integerBreak(self, N):
        """
        :type n: int
        :rtype: int
        """

        memo = [0] * (N+1)
        memo[1] = 1
        memo[2] = 1

        for n in range(3, N+1):
            max_prod = 0
            for cut in range(2, n):
                rest = n - cut
                max_prod = max(max_prod, cut * rest, cut * memo[rest])
            
            memo[n] = max_prod

        return memo[N]
        
