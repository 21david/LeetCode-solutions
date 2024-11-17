# https://leetcode.com/problems/zero-array-transformation-i
# Solution post: https://leetcode.com/problems/zero-array-transformation-i/solutions/6053242/line-sweep-beats-100-commented-code/

# Line Sweep algorithm
from sortedcontainers import SortedDict
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:

        # Build tree
        sd = SortedDict()
        for l, r in queries:
            sd[l] = sd.get(l, 0) + 1
            sd[r+0.1] = sd.get(r+0.1, 0) - 1

        # Iterate through keys in ascending order, calculating new possible value of nums for each index in nums
        curr_idx = 0
        overlaps = 0
        for idx_key, val in sd.items():
            if val < 0:
                # If it's the end of an interval, decrease numbers first
                # then adjust overlaps
                while curr_idx <= idx_key:
                    nums[curr_idx] -= overlaps
                    curr_idx += 1
                overlaps += val
            else:
                # If it's the start of an interval, adjust overlaps first
                # then decrease numbers
                overlaps += val
                while curr_idx <= idx_key:
                    nums[curr_idx] -= overlaps
                    curr_idx += 1


        # Return true if all numbers were decreased to 0 or less
        return all(num <= 0 for num in nums)
            
