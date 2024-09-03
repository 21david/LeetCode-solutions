# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk

'''
Simulation solution
TC: O(N)
  N + N
SC: O(1)
'''
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk_per_round = sum(chalk)

        # Skip rounds where chalk does not run out
        remainder = k % total_chalk_per_round

        # Simulate the last round, where the chalk runs out
        for student_number, chalk_used in enumerate(chalk):
            # Student uses his amount of chalk
            remainder -= chalk_used
            if remainder < 0:
                # This student reached negative, means he ran out and has to replace
                return student_number


'''
Solution using binary search

TC: O(N)
  N + logN
SC: O(N)
'''
from bisect import bisect
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # For each student, calculate total amount of chalk used by all previous
        # students plus the current student for the first round of problems
        total_chalk_used = []
        total_so_far = 0
        for student_number, chalk_used in enumerate(chalk):
            total_so_far += chalk_used
            if total_so_far > k:
                # If the chalk runs out in this first round, we can return early
                return student_number
            total_chalk_used.append(total_so_far)

        # Skip rounds where chalk does not run out
        # Last element in the array represents the total sum of chalk
        remainder = k % total_chalk_used[-1]

        # Figure out at which student does the total amount of chalk used
        # exceed the remaining chalk left. If it exceeds the remainder chalk,
        # it means that student would be the one that runs out.
        return bisect(total_chalk_used, remainder)
