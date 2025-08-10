# TC = O(1) ?
# SC = O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Compute log (base 2) of n. if it is an integer, return True. This is the best way I know to check if it's an integer.
        return log(n, 2) % 1 < 0.000000001 if n > 0 else False

# TC = O(logN)
# SC = O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        test = 1
        while test <= n:
            if test == n:
                return True
            test <<= 1
        
        return False
