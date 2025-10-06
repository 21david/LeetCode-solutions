"""  
Binary search approach, thought of this in maybe ~5 minutes, spent ~25 thinking of a better
approach but didn't find.

Find the max value in the array (or use n^2).
Find half of that, do flood fill on (0,0) to see if it can reach bottom-right
with only cells ≤ that value. If not, increase. If it can, decrease until it can't.
Find the exact smallest value that allows the goal using BS.

TC = O(N^2 log N^2)
SC = O(N^2) if using DFS.
    Can be optimized to O(N) with BFS I think

With the low constraints, I think a brute force would work:
for each t from 0 - n^2, do a flood fill to check if the bottom right can be reached.
TC = O(N^3)
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # O(N^2) - check if there is a path from (0,0) to (n-1,n-1) with t water level
        def can_swim(t):
            if grid[0][0] > t:
                # Don't forget to check current cell
                return False
            return can_swim_helper(0,0, t, set())

        def can_swim_helper(r, c, t, visited):
            if (r,c) == (n-1,n-1):
                return True

            dirs = ((1,0), (-1,0), (0,1), (0,-1))

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if n > nc >= 0 <= nr < n and (nr,nc) not in visited and grid[nr][nc] <= t:
                    visited.add((nr,nc))
                    if can_swim_helper(nr, nc, t, visited):
                        return True
            
            return False


        # BINARY SEARCH
        lo = 0
        hi = n * n

        while lo <= hi:
            t = lo + (hi - lo) // 2

            if can_swim(t):
                print(f"{t} works")
                hi = t - 1
            else:
                print(f"{t} doesnt works")
                lo = t + 1

        print(hi,lo)
        
        return lo

