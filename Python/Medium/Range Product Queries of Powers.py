# TC = O(Q + logN), logN for creating powers (check each bit of n), Q for processing the queries
# Aux SC = O(logN), for powers, which stores up to as many numbers as bits in n
# Output SC = O(Q)
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Powers = just the bits that are set in n. Start with 1 to turn it into prefix product array later.
        powers = [1]
        bit = 1
        while bit <= n:
            if n & bit:
                powers.append(bit)
            bit <<= 1

        # Use prefix sum array to quickly compute queries
        powers = list(accumulate(powers, operator.mul))

        ans = []
        mod = 10 ** 9 + 7

        for left, right in queries:
            ans.append((powers[right+1] // powers[left]) % mod)

        return ans

