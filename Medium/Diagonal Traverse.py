"""
https://leetcode.com/problems/diagonal-traverse

So I think the approach for this is you start at the top left, and you try to move 
up-right. Once you reach the limit, try to move right; if you can't, then try to move 
down. Once you've moved, you switch directions and go down-left. When you reach the 
border, try to move down initially, and if you can't, then try to move right. Repeat 
this process, and when you can't move either right or down and you've reached the 
bottom right corner, you're done.

TC: O(R * C)
Auxiliary SC: O(1)
"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R = len(mat)
        C = len(mat[0])
        answer = []

        # Current direction
        dr, dc = -1, 1

        # Current position
        r, c = 0, 0

        while True:
            answer.append(mat[r][c])

            # Try to continue going in current direction
            if (0 <= (r + dr) < R) and (0 <= (c + dc) < C):
                r += dr
                c += dc
            # If you're at the border move to the next diagonal and switch direction
            else:
                # Determine where the next diagonal is
                if (c == C-1) and (r == R-1):
                    break
                elif r == R-1:
                    c += 1
                elif c == C-1:
                    r += 1
                elif r == 0:
                    c += 1
                elif c == 0:
                    r += 1
                
                # Switch the direction
                dr *= -1
                dc *= -1

        return answer


