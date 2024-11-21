class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        available = m * n

        # Set guards and walls to -1
        for r, c in guards + walls:
            grid[r][c] = -1
            available -= 1

        # Iterate through each cell each guard can see
        for guard_r, guard_c in guards:
            # Go north
            temp_r = guard_r - 1
            while temp_r >= 0:
                match grid[temp_r][guard_c]:
                    case -1:  # Another guard or wall
                        break
                    case 0:  # Unseen cell
                        available -= 1
                        grid[temp_r][guard_c] = 1
                    case 1:  # Seen cell
                        pass
                temp_r -= 1

            # Go south
            temp_r = guard_r + 1
            while temp_r < m:
                match grid[temp_r][guard_c]:
                    case -1:  # Another guard or wall
                        break
                    case 0:  # Unseen cell
                        available -= 1
                        grid[temp_r][guard_c] = 1
                    case 1:  # Seen cell
                        pass  # pass over it
                temp_r += 1

            # Go west
            temp_c = guard_c - 1
            while temp_c >= 0:
                match grid[guard_r][temp_c]:
                    case -1:  # Another guard or wall
                        break
                    case 0:  # Unseen cell
                        available -= 1
                        grid[guard_r][temp_c] = 1
                    case 1:  # Seen cell
                        pass  # pass over it
                temp_c -= 1

            # Go east
            temp_c = guard_c + 1
            while temp_c < n:
                match grid[guard_r][temp_c]:
                    case -1:  # Another guard or wall
                        break
                    case 0:  # Unseen cell
                        available -= 1
                        grid[guard_r][temp_c] = 1
                    case 1:  # Seen cell
                        pass  # pass over it
                temp_c += 1

        return available
