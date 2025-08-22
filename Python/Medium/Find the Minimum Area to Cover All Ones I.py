# Check for rows and cols with all 0s
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        # Check rows starting from the top. Stop as soon as a row has a 1.
        top_rows = 0
        top_rows_ct = 0
        while True:
            found_one = False
            for i in range(C):
                if grid[top_rows][i]:
                    found_one = True
                    break
            if found_one:
                break
            top_rows += 1
            top_rows_ct += 1

        # Check rows starting from the bottom. Stop as soon as a row has a 1.
        bot_rows = R - 1
        bot_rows_ct = 0
        while True:
            found_one = False
            for i in range(C):
                if grid[bot_rows][i]:
                    found_one = True
                    break
            if found_one:
                break
            bot_rows -= 1
            bot_rows_ct += 1

        # Check cols starting from the left. Stop as soon as a col has a 1.
        left_cols = 0
        left_cols_ct = 0
        while True:
            found_one = False
            for i in range(R):
                if grid[i][left_cols]:
                    found_one = True
                    break
            if found_one:
                break
            left_cols += 1
            left_cols_ct += 1

        # Check cols starting from the right. Stop as soon as a col has a 1.
        right_cols = C - 1
        right_cols_ct = 0
        while True:
            found_one = False
            for i in range(R):
                if grid[i][right_cols]:
                    found_one = True
                    break
            if found_one:
                break
            right_cols -= 1
            right_cols_ct += 1

        print(top_rows_ct, bot_rows_ct, left_cols_ct, right_cols_ct)

        min_width = C - left_cols_ct - right_cols_ct
        min_height = R - top_rows_ct - bot_rows_ct

        return min_width * min_height

