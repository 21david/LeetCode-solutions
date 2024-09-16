# https://leetcode.com/problems/maximum-multiplication-score

# Recursive solution
# TC: O(2^len(b))
# SC: O(len(b))
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        max_sum = -math.inf

        def subsets(i, left, curr_sum):
            nonlocal max_sum
            if left == 0:
                max_sum = max(max_sum, curr_sum)
                # print(curr_sum)
                return
            elif i >= len(b):
                return

            # include
            subsets(i+1, left-1, curr_sum + a[4-left] * b[i])

            # exclude
            subsets(i+1, left, curr_sum)

        subsets(0, 4, 0)
        return max_sum

