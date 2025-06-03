'''
https://leetcode.com/problems/continuous-subarrays

After reading Priority Queue solution in editorial.

TC: O(N log N)
SC: O(N)
'''
from heapq import heapify, heappop as pop, heappush as push
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minh = []
        maxh = []

        ans = 0
        l = 0
        for r in range(len(nums)):
            push(minh, (nums[r], r))
            push(maxh, (-nums[r], r))

            while abs(minh[0][0] + maxh[0][0]) > 2:
                # Window needs to be fixed
                l += 1

                while minh[0][1] < l:
                    pop(minh)
                
                while maxh[0][1] < l:
                    pop(maxh)

            # Window should be fixed
            ans += r - l + 1

        return ans
