# https://leetcode.com/problems/add-minimum-number-of-rungs/description/
# Greedy: Add the necessary rungs whenever needed. Use math to calculate number of
# rungs in O(1). 
# TC: O(N)
# SC: O(1)
class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pos = ans = 0
        for rung in rungs:
            if rung - pos > dist:
                ans += (rung - 1 - pos) // dist
            pos = rung
        return ans
