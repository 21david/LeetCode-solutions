# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums

class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        """
        Approach:
        Create a 2D matrix of the given size (len(rowSum) * len(colSum)), filled with 0s.
        Travel through the diagonal from position (0,0) until reaching the limit 
        (min(len(R), len(C)) - 1). In each iteration, take the minimum of the sums for 
        that row and column. Put that number in that cell. If the sums are equal, then 
        there is no 'remainder' and we can move to the next iteration. If the minimum was 
        the rowSum, distribute the remainder (colSum[i] - rowSum[i]) in the rest of the
        column. If the minimum was the columnSum, distribute the remainder in the rest of 
        the row. To distribute, we can follow a greedy approach where we fill in as much 
        as we can with each cell we pass (left to right or top to bottom), until the 
        remainder is 0. Every time we fill in a cell, we have to update the sum for that
        row or column by subtracting what we just added to the matrix from both sum arrays. 
        This approach will automatically fill in all the numbers that satisfy all the row 
        and column sums, for matrices of all shapes and sizes.

        Time complexity:
        Assuming N = len(rowSum) and M = len(colSum).
        Best case scenario: We just travel through the diagonal of a matrix and assign only
        those numbers. This would be O(min(N, M)), however, creating the matrix to store the
        answer in is still O(N * M) to create and assign each cell.
        Worst case scenario: For every row or column, we have to distribute many times (a 
        fraction of N or M). This would be O(N * M).
        In both cases, the time complexity is O(N * M).

        Space complexity:
        Input space complexity: O(N + M)
        Auxiliary space complexity: O(1). We only use memory for R, C, i, j, and remainder.
        Output space complexity: O(N * M). We need a full matrix to store the final answer.
        """
        R = len(rowSum)
        C = len(colSum)
        ans = [[0] * C for _ in range(R)]

        for i in range(min(R, C)):
            if rowSum[i] == colSum[i]:
                # Fill in the current cell
                ans[i][i] = rowSum[i]
            elif rowSum[i] < colSum[i]:
                # Fill in the current cell
                remainder = colSum[i] - rowSum[i]
                ans[i][i] = rowSum[i]

                # Distribute the remainder across the rest of the column
                j = i + 1
                while j < R:
                    if remainder <= rowSum[j]:
                        # If the entire remainder fits in the next cell, put it there and continue
                        ans[j][i] = remainder
                        rowSum[j] -= remainder
                        break
                    else:
                        # If it doesn't fit, fill in as much as possible, and move to the next cell
                        ans[j][i] = rowSum[j]
                        remainder -= rowSum[j]
                        rowSum[j] = 0
                        j += 1
            
            else:  # colSum[i] has the smaller number
                # Fill in the current cell
                remainder = rowSum[i] - colSum[i]
                ans[i][i] = colSum[i]

                # Distribute the remainder across the rest of the row
                j = i + 1
                while j < C:
                    if remainder <= colSum[j]:
                        # If the entire remainder fits in the next cell, put it there and continue
                        ans[i][j] = remainder
                        colSum[j] -= remainder
                        break
                    else:
                        # If it doesn't fit, fill in as much as possible, and move to the next cell
                        ans[i][j] = colSum[j]
                        remainder -= colSum[j]
                        colSum[j] = 0
                        j += 1
        
        return ans


        
