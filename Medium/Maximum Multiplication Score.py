# https://leetcode.com/problems/maximum-multiplication-score

# Recursive solution
# TC: O(2^len(b))
# SC: O(len(b))
# TLE 547/672
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        max_sum = -math.inf

        def subsets(i, left, curr_sum):
            nonlocal max_sum
            if left == 0:
                max_sum = max(max_sum, curr_sum)
                return
            elif i >= len(b):
                return

            # include
            subsets(i+1, left-1, curr_sum + a[4-left] * b[i])

            # exclude
            subsets(i+1, left, curr_sum)

        subsets(0, 4, 0)
        return max_sum

# Another recursive solution
# Builds the sum as it backtracks out of recursive calls,
# rather than while it makes recursive calls like above
# TLE 551/672
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        def subsets(i, left):
            if left == 0:
                return 0
            elif i >= len(b):
                # If ran out before finishing, this can't be an answer
                return -math.inf

            max_if_include = subsets(i+1, left-1) + a[4-left] * b[i]

            max_if_exclude = subsets(i+1, left)

            return max(max_if_include, max_if_exclude)

        return subsets(0, 4)

'''
Add memoization:
As i iterates through b, there will be a maximum sum for each amount of
numbers picked for every index i. For example, if it's halfway through b
and it has picked 2 numbers, then there is a maximum sum for having picked
two numbers at that point, as well as 0, 1, 3, and 4. 
If we store the maximum sum at that index and number of numbers picked, then
as we pick the rest of the numbers, we can use the maximum instead of
re-exploring every combination, which reduces work.

Solved with seeing solutions
'''
class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        @cache
        def subsets(i, left):
            if left == 0:
                return 0
            elif i >= len(b):
                # If ran out before finishing, this can't be an answer
                return -math.inf

            max_if_include = subsets(i+1, left-1) + a[4-left] * b[i]

            max_if_exclude = subsets(i+1, left)

            return max(max_if_include, max_if_exclude)

        return subsets(0, 4)
