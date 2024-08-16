# https://leetcode.com/problems/sum-of-square-numbers/

'''
Solution 1
Memory Limit Exceeded
Create a set with all perfect squares from 0 to the smallest one that is
less than or equal to c.
For every pair of non-negative numbers a and b such that a + b = c, 
check if a and b are both perfect squares by looking them up in the set.
Return true if it they are, return false if there is no pair found.
'''
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        squares = set(x**2 for x in range(int(sqrt(c)+1)))

        for i in range( c+1):
            if i in squares and c-i in squares:
                return True

        return False


'''
Solution 2:
Attempt to subtract every square that is <= c.
Check if the remainder is a square. If it is,
then those are the 2 squares that sum to c, and we
can return true. If it runs out of squares (including 0),
we return false.
Much more time and space efficient than the solution above.
'''
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        def is_perfect_square(n):
            return int(sqrt(n))**2 == n

        for n in range(int(sqrt(c)), -1, -1):
            if is_perfect_square(c - n**2):
                return True
        
        return False
