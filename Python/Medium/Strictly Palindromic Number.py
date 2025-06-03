# https://leetcode.com/problems/strictly-palindromic-number
# See my write-up here: https://leetcode.com/problems/strictly-palindromic-number/solutions/5652370/python-zero-line-solution/

class Solution:
    def isStrictlyPalindromic(self, n):
        '''
        My first intuition was that it seems that between any two bases with a difference
        of 1, the number changes by only 1. Example: 10 in base 7 is '13', then in base 6
        it's 14. How can a number stay a palindrome if it changes by only the rightmost number
        for every base?

        Another way to think is by using the way bases work. Any number N is represented
        by 10 in base-N.
        These are the values of each position in base-N. When filled in with values (symbols
        from 0 to N-1), you multiply that value with the value of it's position.

        N^2  N^1  N^0
        [ ]  [ ]  [ ]
        or equivalently:
        N^2   N    1
        [ ]  [ ]  [ ]

        so 10 (base-N) = N * (1) + 1 * (0) 
        N^2   N    1
        [ ]  [1]  [0]

        Now, take base N-1. The value for the second column (from the right) decreases by 1.
        To represent the same number, now you need to push a 1 to the first column (ones column).
        So the number will become '11'.

        Now base N-2, which is the first one that can be considered for the problem.
        The value for the second column decreases by 2. Now you need to push 2 over to the
        ones column, resulting in '12'. 

        Since this is a variable, then it will apply to any actual number for N. So every
        number will be represented as 10 in base N, 11 in base N-1, 12 in base N-2, 13 in
        base N-3, and so forth, except the smaller numbers where N-2 is already base 2 or lower.

        My second thought was if there were any exceptions for the smallest numbers. The
        smallest number that can be the input is 4, which makes sense because base n-2 would 
        be 2, which is pretty much the lowest base.

        4 == 10 (base4)
          == 11 (base3)
          == 100 (base2)

        5 == 10 (base5)
          == 11 (base4)
          == 12 (base3)
          == 101 (base2)

        6 == 10 (base 6) 
          == 11 (base 5)
          == 12 (base 4) 
          == 20 (base 3) 
          == 110 (base 2)

        7 == 10 (base 7) 
          == 11 (base 6) 
          == 12 (base 5) 
          == 13 (base 4) 
          == 21 (base 3) 
          == 111 (base 2)
        
        None can ever be strictly palindromic and its easy to see the pattern.

        If the question allowed leading 0s, then 4 would be the only one.
        Unless base 1 was allowed, then 3 would also work.
        If base 0 was a thing and it could only represent nothing, perhaps 2
        would also work?

        There is no number N that satisfies the 'strictly palindromic' definition, so the output 
        of this function cannot be anything other than false. We can use the fact that Python considers 
        None as a falsy value, and that it returns None by default if a return statement is not added.
        Therefore, no code needs to be written after this comment block to pass all test cases correctly.
        '''
        
