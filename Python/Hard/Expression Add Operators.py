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
Time complexity: O(4^N * N) because each recursive call makes 4 recursive calls, which creates a tree.
At the base cases (about 4^(N-1) of these), O(N) work is performed to evaluate the expression.
Space complexity: O(4^N * N). In the worst case, nearly all 4^(N-1) attempted expressions will
be a valid expression, and each expression will take space for anywhere between N and 2N-1 characters.
The space complexity used for the stack is O(N).
This attempt exceeds the time limit on LeetCode because of the functions to evaulate the expression at the end. See the next 
solution for an approach that passes.
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



"""
Solution 2:
The same approach as above, but as we are building the expressions, we calculate the current value
of it, instead of calculating each one at the end. We also check for and avoid leading 0s as we're
building the expression.
To evaluate the expression as we're going, we must do something different when multiplying than when
adding or subtracting because of the priority of multiplication (PEMDAS). One way to do this is to 
keep track of the previous operand (the last one that has been fully read). With that, if you need 
that operand for a multiplication rather than a sum or subtraction, then you can undo it from the 
current expression value (stored in a variable), use it for the multiplication, and then recalculate 
the total. The exception to this is that when multiplying, it should accumulate the product of 
multiple multiplications in a row for it to work.

Time complexity: O(4^N * N) because each recursive call makes 4 recursive calls, which creates a tree.
Each recursive call creates a new string, which is an O(N) operation because strings are immutable.

Space complexity: O(4^N * N). In the worst case, nearly all 4^(N-1) attempted expressions will
be a valid expression, and each expression will take space for anywhere between N and 2N-1 characters.
The space complexity used for the call stack is O(N).
"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        helper(
            num,        # s
            [num[0]],   # slate
            0,          # curr_total
            0,          # prev_num
            num[0],     # curr_num
            1,          # i
            False,      # multiplying
            target,     # target
            ans         # ans
        )

        return ans

# num - (string) the original number
# slate - (list of strings) temporary variable to store the expression as we build it
# curr_total - (integer) current value of the expression so far
# prev_num - (integer) the previous integer/operand that has been fully read
# curr_num - (string) the current integer/operand that is being read
# i - (integer) the index of the current letter we are considering
# target - (integer) the target value
# ans - (array of strings) array to store the final answers
def helper(num, slate, curr_total, prev_num, curr_num, i, multiplying, target, ans):
    if i == len(num): # reached the end of the string
        # Calculate new total and compare with target
        new_total = None
        if multiplying:
            new_total = (curr_total - prev_num) + (prev_num * int(curr_num))
        else:
            new_total = curr_total + int(curr_num)

        if new_total == target:
            ans.append(''.join(slate))

        return
    
    # If our current number is a 0, we can't add more numbers because
    # we can't have trailing 0s
    if not (curr_num == '0' or curr_num == '-0'):
        slate.append(num[i])
        helper(
            num,              
            slate,
            curr_total,         # curr_total
            prev_num,           # prev_num
            curr_num + num[i],  # curr_num
            i+1,                # i
            multiplying,        # operator
            target,             
            ans
        )
        slate.pop()

    # If we're not joining, then we're ending the number and starting a new number
    # so the value of curr_total has to change
    new_total = 0
    new_prev_num = 0
    if multiplying:
        new_total = (curr_total - prev_num) + (prev_num * int(curr_num))
        new_prev_num = prev_num * int(curr_num)
    else:
        new_total = curr_total + int(curr_num)
        new_prev_num = int(curr_num)

    slate.extend(['+', num[i]])
    helper(
        num, 
        slate,
        new_total,              # curr_total
        int(new_prev_num),      # prev_num 
        num[i],                 # curr_num
        i+1,                    # i
        False,                  # multiplying
        target, 
        ans
    )

    slate[-2] = '*'
    helper(
        num, 
        slate,
        new_total,              # curr_total 
        int(new_prev_num),      # prev_num
        num[i],                 # curr_num
        i+1,                    # i 
        True,                   # multiplying
        target, 
        ans
    )

    slate[-2] = '-'
    helper(
        num, 
        slate,
        new_total,              # curr_total
        int(new_prev_num),      # prev_num
        '-' + num[i],           # curr_num 
        i+1,                    # i
        False,                  # multiplying
        target, 
        ans
    )
    slate.pop(); slate.pop()
