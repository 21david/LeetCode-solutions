# https://leetcode.com/problems/clumsy-factorial

class Solution(object):
    def clumsy(self, n):
        '''
        since the order is the same, we can predict the future operations. 
        so whenever we do the multiplication and division, we can store the
        result of that in a buffer. then when we get to the addition, we either
        add or subtract what's in the buffer to the grand total. if it's the 
        first time we've done the multiplication and division part, then we add
        it to the grand total because the result should be positive. if it's 
        the second or more time that we do the multiplication and division part, 
        then we subtract it from the grand total because the operation before 
        that was subtract, which makes the result nrgative. 
        
        another approach would be to do the first four numbers manually and then 
        do all the others in the loop, which would be easier because the loop 
        would only have to worry about subtracting the multiplication and division
        results.

        TC: O(N) 
        SC: O(1)
        '''
        total = 0
        buffer = n
        n -= 1
        i = 0

        while n:
            if i % 4 == 0:  # *
                buffer *= n
            elif i % 4 == 1:  # //
                buffer //= n
            elif i % 4 == 2:  # +
                if total: 
                    total -= buffer
                else:      
                    total += buffer
                total += n
                buffer = 0
            elif i % 4 == 3:  # -
                buffer = n

            i += 1
            n -= 1

        if total:
            return total - buffer
        else:
            return total + buffer

'''
Creative version written with ChatGPT. Same approach as above.
'''
class Solution:
    def clumsy(self, n: int) -> int:
        if n <= 2:
            return n
        elif n == 3:
            return 3 * 2

        def operation_generator():
            while True:
                yield lambda total, buffer, n: (total - buffer + n, 0)  # subtract and reset buffer
                yield lambda total, buffer, n: (total, buffer + n)  # Add
                yield lambda total, buffer, n: (total, buffer * n)  # Multiply
                yield lambda total, buffer, n: (total, buffer // n) # Integer division
        
        total = n * (n-1) // (n-2)
        buffer = 0
        n -= 2
        i = 2

        operations = operation_generator()

        while n := n - 1:
            total, buffer = next(operations)(total, buffer, n)

        return total - buffer
