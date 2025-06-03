'''
LeetCode January 11, 2025 contest.
Dynamic programming top-down solution.
'''
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        R, C = len(coins), len(coins[0])
        
        @cache
        def dfs(r, c, left):
            if r < 0 or r >= R or c < 0 or c >= C:
                return -math.inf

            if (r,c) == (R-1,C-1):
                if coins[r][c] < 0 and left >= 1:
                    return 0
                else:
                    return coins[r][c]

            down2 = right2 = -math.inf
            
            if coins[r][c] >= 0:
                down = dfs(r+1, c, left) + coins[r][c]
                right = dfs(r, c+1, left) + coins[r][c]
                return max(down, right)

            else:
                if left <= 0:
                    down = dfs(r+1, c, left) + coins[r][c]   # don't neutralize
                    right = dfs(r, c+1, left) + coins[r][c]   # don't neutralize
                    return max(down, right)
                else:
                    down = dfs(r+1, c, left) + coins[r][c]   # don't neutralize
                    right = dfs(r, c+1, left) + coins[r][c]   # don't neutralize
                    down2 = dfs(r+1, c, left - 1)   # neutralize
                    right2 = dfs(r, c+1, left - 1)   # neutralize
                    return max(down, right, down2, right2) # + (coins[r][c]) # if coins[r][c] >= 0 else 0)


        return dfs(0, 0, 2) 
