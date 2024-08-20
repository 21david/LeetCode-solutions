# https://leetcode.com/problems/rotate-image

'''
After an educated guess and by drawing it, I found that you can have 2 pointers. One starts
at the top-left and the other at the bottom-left. They swap, then the first pointer
moves down and the second pointer moves to the right. When they reach the other side,
they will move to the next wall, following the edge of the square. It takes n * 2
iterations of this to swap one layer of the square (a layer is an inner square
with width of 1). This can then be done on all the inner layers until done.

TC would be O(R*C), (num rows * num columns) to perform a swap on each square.
SC would be O(1). Only 1 temporary variable is needed to store values while swapping.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        # For all the layers (layers 1 to N//2 inclusive)
        for layer in range(1, N//2+1):
            # Turn to the next direction after this amount of swaps
            turn_every = N - (layer-1)*2 - 1
            a_row, a_col = layer-1, layer-1  # row and col pointer for a, start at top-left
            b_row, b_col = (N-layer), layer-1  # row and col pointer for b, start at bottom-left

            # Keep going until b reaches the point where a started, at which point, it will
            # have cycled through the entire layer exactly once and rotated it
            i = 0   # used for switching directions
            while [b_row, b_col] != [layer-1,layer-1]:
                # Swap
                matrix[a_row][a_col], matrix[b_row][b_col] =  matrix[b_row][b_col], matrix[a_row][a_col]
                
                # Figure out where to move pointers
                # Every (L-1) times, where L is the length of the current square/layer
                # the pointers will switch directions
                a_row_change, a_col_change = dirs[i // turn_every ]
                b_row_change, b_col_change = dirs[i // turn_every + 1]

                # Move pointers
                a_row += a_row_change
                a_col += a_col_change
                b_row += b_row_change
                b_col += b_col_change

                i += 1
