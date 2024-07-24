# https://leetcode.com/problems/expression-add-operators

"""
Solution 1:
Go from left to right, and between every 2 numbers, try the following operations: join, add, subtract, multiply.
Join will just combine two numbers, like 1 and 2 into 12. Try all combinations of these 4 operations for all digits in the number,
and this will create every possible valid expression with every possible set of operands and operators.
This is basically a brute force approach, which is necessary because we can't know what the final result of an expression will be 
without trying. For each attempt, once we reach the end of the string and have an expression, we evaluate it, and if it evaluates 
to the target, we keep the expression in an array that is returned at the end. Then, we filter out the solutions that have a
number with a leading 0.

This attempt exceeds the time limit on LeetCode because of the functions to evaulate the expression at the end.
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        helper(num, num[0], 1, target, ans)

        # Remove answers with leading 0s
        ans = [str for str in ans if no_leading_zeros(str)]

        return ans

import re
def no_leading_zeros(s):
    nums = re.split(r'[*+-]', s)
    for num in nums:
        if len(num) > 1 and num[0] == '0':
            return False
    return True

# s - the original string
# slate - temporary variable to store the expression as we build it
# l - the index of the current letter we are considering
# target - the target value
# ans - array to store the final answers
def helper(s, slate, l, target, ans):
    if l == len(s): # reached the end of the string
        # Keep this expression if it evaluates to target
        if eval_sum(eval_mult(slate)) == target:
            ans.append(slate)
        return
    
    helper(s, slate + s[l], l+1, target, ans)
    helper(s, slate + '+' + s[l], l+1, target, ans)
    helper(s, slate + '-' + s[l], l+1, target, ans)
    helper(s, slate + '*' + s[l], l+1, target, ans)
    
# Solve and remove all multiplication operators
# Example: 1+2+2*4*5+8 -> 1+2+40+8
def eval_mult(exp):
    l = 0 # left (start of multiplication expression)
    r = 1 # right (end of multiplication expression)
    m = None # index of multiplication operator
    
    while r < len(exp):
        if exp[r] == '+' or exp[r] == '-':
            l = r + 1
        elif exp[r] == '*':
            m = r
            r += 1
            while r < len(exp) and exp[r].isdigit():
                r += 1
            # We know locations of the start of the first number, the multiplication
            # operator, and the end of the last number. With these, we can multiply.
            product = int(exp[l:m]) * int(exp[m+1:r])
            exp = exp[:l] + str(product) + exp[r:]
            r = l # fix index of r after editing 'exp'
        r += 1
        
    return exp

# Solve and remove all + and - operators, resulting in one final integer
# Example: 1+3-4-2 -> -2
def eval_sum(exp):
    nums = exp.split('+')
    total_sum = 0
    for str in nums:
        if str.find('-') >= 0:
            nums2 = str.split('-')
            total_sum += int(nums2[0])
            for i in range(1, len(nums2)):
                total_sum -= int(nums2[i])
        else:
            total_sum += int(str)
    return total_sum
