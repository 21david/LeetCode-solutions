'''
TC = O(R * C), all cells are visited 1 or 2 times
SC = O(R * C), dfs call stack may include all cells in the worst case
This could be optimized to O(min(R, C)) with a BFS since it would only store
a maximum of about one diagonal at a time
'''
class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        count = 0

        def in_bounds(r, c):
            return R > r >= 0 <= c < C

        def explore_and_delete(r, c):  # DFS
            nonlocal island_sum
            if not in_bounds(r, c) or grid[r][c] == 0:
                return

            island_sum += grid[r][c]
            grid[r][c] = 0  # Delete cell

            explore_and_delete(r-1, c)
            explore_and_delete(r+1, c)
            explore_and_delete(r, c-1)
            explore_and_delete(r, c+1)

        # Traverse matrix looking for islands
        island_sum = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] >= 1:
                    # Found an island, process and delete it
                    explore_and_delete(r, c)
                    count += island_sum % k == 0
                    island_sum = 0

        return count
