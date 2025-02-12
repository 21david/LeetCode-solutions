# After seeing solution post: count number of left edges
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/754682/wall-of-bricks/
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]

        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                ans += target[i] - target[i-1]

        return ans
