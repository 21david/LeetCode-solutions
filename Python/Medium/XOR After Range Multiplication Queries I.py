# Simple brute force solution
# Does 10^3 * 10^3 = 10^6 operations at the most
# TC = O(N * Q)
# SC = O(1)
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                nums[i] = (nums[i] * v) % mod

        return reduce(operator.xor, nums, 0)
