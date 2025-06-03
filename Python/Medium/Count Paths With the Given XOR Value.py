# Dynamic programming
class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        M, N = len(grid), len(grid[0])

        if M == N == 1:
            return int(grid[0][0] == k)

        memo = {}
        totals = [[0] * N for _ in range(M)]

        def dfs(r, c, acc):
            if r >= M or c >= N:
                return 0

            acc ^= grid[r][c]

            if (r, c, acc) in memo:
                return memo[(r, c, acc)]

            if r == M - 1 and c == N - 1:
                return acc == k

            down = dfs(r + 1, c, acc)
            right = dfs(r, c + 1, acc)
            res = down + right
            memo[(r, c, acc)] = res
            totals[r][c] += res
            return res

        dfs(0, 0, 0)
        return totals[0][0] % int(1e9 + 7)
