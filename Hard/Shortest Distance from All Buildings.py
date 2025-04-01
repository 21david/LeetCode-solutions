"""  
BFS (or A* ?) starting from each building to get min distance to every cell
on the grid. Store results in another matrix. Once done with all buildings,
just take the min in the matrix.

TC: O((R * C)^2) AKA O((M * N)^2)
    if # of buildings is known, O(B * R * C)
SC: O(R * C) AKA O(M * N)
"""
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # Set up matrix to store accumulated distances
        distances = [[0] * C for _ in range(R)]
        for r, c in product(range(R), range(C)):
            distances[r][c] = math.inf if grid[r][c] else 0

        buildings = [[0] * C for _ in range(R)]
        num_buildings = 0

        def bfs(start_r, start_c):
            q = deque([(start_r, start_c, 0)])
            visited = set((start_r, start_c))

            while q:
                r, c, d = q.popleft()
                distances[r][c] += d
                buildings[r][c] += 1

                # Visit all neighboring unexplored 0s
                neis = [[r,c+1], [r+1,c], [r,c-1], [r-1,c]]
                for new_r, new_c in neis:
                    if R > new_r >= 0 <= new_c < C and grid[new_r][new_c] == 0 and (new_r, new_c) not in visited:
                        q.append((new_r, new_c, d+1))
                        visited.add((new_r, new_c))

        # Do BFS on every building to accumulate shortest distance to every cell on the grid
        for r, c in product(range(R), range(C)):
            if grid[r][c] == 1:
                num_buildings += 1
                bfs(r, c)

        # print(str(distances).replace('], ', '],\n ').replace('inf', '∞'))
        # print(str(buildings).replace('], ', '],\n '))

        # Find minimum in the whole matrix. The cell must be able to reach all
        # buildings to be considered.
        min_dist = math.inf
        for r, c in product(range(R), range(C)):
            if buildings[r][c] == num_buildings:
                min_dist = min(min_dist, distances[r][c])

        return min_dist if min_dist < math.inf else -1
