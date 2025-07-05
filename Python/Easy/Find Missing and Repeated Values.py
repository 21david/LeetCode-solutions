class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        cts = [0] * N ** 2
        for r in range(N):
            for c in range(N):
                cts[grid[r][c] - 1] += 1

        ans = [0,0]

        for i in range(len(cts)):
            if cts[i] == 2:
                ans[0] = i + 1
            elif cts[i] == 0:
                ans[1] = i + 1

        return ans
