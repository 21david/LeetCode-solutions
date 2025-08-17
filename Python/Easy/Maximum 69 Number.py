# String solution
# TC = O(logN), log base 10
# Aux SC = O(logN), log base 10
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        for i, c in enumerate(num_str):
            if c == '6':
                return int(num_str[:i] + '9' + num_str[i+1:])  # could be optimized with list, loops, and join()
        return num


# Math solution
# TC = O(logN), log base 10
# Aux SC = O(1)
class Solution(object):
    def maximum69Number (self, num):
        """
        Try to change the leftmost 6 into a 9.
        If there are no 6s, change nothing.
        """
        
        mod = 1
        
        while mod < num:
            mod *= 10
            
        m = mod / 10
        
        # Traverse the digits from left to right
        while m > 0:
            # Isolate the current digit we're at
            if ((num % mod) - (num % m)) / m == 6:
                # Replace with a 9
                num -= (num % mod) - (num % m)
                num += 9 * m
                break   # we can only change 1
            mod /= 10
            m /= 10
            
        return num
        
