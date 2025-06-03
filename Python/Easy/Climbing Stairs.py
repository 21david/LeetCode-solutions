# https://leetcode.com/problems/climbing-stairs/
# Solved in 10 minutes

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # For n steps, it takes [nth fibonacci number] to get to the top
        # if the Fibonacci sequence starts with 1, 2
        if n == 1:
            return 1

        a = 1
        b = 2

        for _ in range(n-2):
            a, b = b, a + b

        return b
