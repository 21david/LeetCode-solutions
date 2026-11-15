import operator
from functools import reduce

# TC = O(N^3)
# SC = O(N)
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        ans = 0
        
        for s in range(len(nums)):
            for e in range(s+1, len(nums)+1):
                subarray = nums[s:e]
                if min(subarray) == reduce(operator.and_, subarray):
                    ans += 1

        return ans
