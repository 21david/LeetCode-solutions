# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_copy = x
        reverse = 0

        while x_copy > 0:
            reverse += x_copy % 10
            x_copy /= 10
            reverse *= 10
                    
        reverse /= 10

        return reverse == x
