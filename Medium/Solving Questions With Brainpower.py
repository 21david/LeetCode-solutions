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


# After seeing editorial
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        Q = len(questions)

        dp = [question[0] for question in questions]
        for i in range(Q-2, -1, -1):
            next_idx = i + questions[i][1] + 1
            solve = dp[i]
            if next_idx < Q:
                solve += dp[next_idx]

            skip = dp[i+1]

            dp[i] = max(solve, skip)

        return dp[0]
