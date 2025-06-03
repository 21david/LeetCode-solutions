"""  
Even indices must contain: 0, 2, 4, 6, 8  =>  That is 5 possibilities
Odds must contain: 2, 3, 5, 7  => That is 4 possibilities
So to find the answer for a number of length n, we do

_ _ _ _ _
5*4*5*4*5

A shortcut is to divide n by 2 to get roughly the number of 5s and 4s in this formula,
then exponentiate to get the answer. If n is odd, the extra spot is always gonna be an
even index so we just multiply by another 5.

    half = n // 2
    answer = (5 ** half) * (4 ** half) * (5 if n is odd)

But n can get very large, so the result of exponentiation could be enormous, so we
need a more efficient way to calculate. Since modulo has some useful properties,
we can make a recursive cached expnentiation function that calculates the result
efficiently. I think the only difference between this version and ** or built in
functions is that this function mods it at each step, keeping the numbers small.
Since modulo has that one special property, this results in the right answer.

TC: O(log2 N)
SC: O(log2 N)

Could be solved with a stack instead of recursion? I think this would be slightly
more memory efficient but still be O(log2 N), and prevent max recursion depth issue
if N were larger.
"""
mod = 10**9 + 7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Efficient exponentiation with mod at each step
        # which prevents numbers from getting too large
        def exp(base, superscript):  # O(log2 superscript)
            if superscript == 1:
                return base
            elif superscript == 0:
                return 1

            half, remainder = divmod(superscript, 2)

            res = exp(base, half) % mod

            res = (res * res) % mod

            if remainder:
                res = (res * base) % mod

            return res

        # Calculate the final answer
        half, remainder = divmod(n, 2)

        res = exp(5, half) * exp(4, half) % mod

        if remainder:
            res = (res * 5) % mod

        return res
