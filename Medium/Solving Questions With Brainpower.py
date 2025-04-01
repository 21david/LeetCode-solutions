class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        Q = len(questions)

        @cache
        def rec(i):
            if i >= Q:
                return 0

            solve = questions[i][0] + rec(i + questions[i][1] + 1)
            skip = rec(i+1)

            return max(solve, skip)

        return rec(0)
