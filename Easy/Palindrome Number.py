# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        x_copy = x
        reverse = x_copy % 10
        x_copy /= 10

        while x_copy:
            reverse *= 10
            reverse += x_copy % 10
            x_copy /= 10

        return reverse == x
