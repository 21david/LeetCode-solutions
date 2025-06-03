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


'''
Recursive versin of the solution above.
Each layer is just a smaller version of the original problem.
'''
class Solution:
    def rotate(self, matrix: List[List[int]], layer: int = 1) -> None:
        N = len(matrix)
        if layer > N//2:
            return

        directions = [(1,0), (0,1), (-1,0), (0,-1)]  # down, right, up, left

        # Turn to the next direction after this amount of iterations
        turn_every = N - (layer-1)*2 - 1

        # Set up the A and B pointers
        a_row, a_col = layer-1, layer-1  # row and col pointer for A, starts at top-left of current layer
        b_row, b_col = N-layer, layer-1  # row and col pointer for B, start at bottom-left of current layer

        # Keep going until B reaches the point where A started, at which point, it will
        # have cycled through the entire layer exactly once and rotated it
        i = 0  # used for switching directions every L times, where L is the length of the current layer
        while [b_row, b_col] != [layer-1,layer-1]:
            # Swap
            matrix[a_row][a_col], matrix[b_row][b_col] =  matrix[b_row][b_col], matrix[a_row][a_col]

            # Figure out where to move pointers
            # Every (L-1) times, where L is the length of the current layer
            # the pointers will switch directions
            a_row_change, a_col_change = directions[i // turn_every]
            b_row_change, b_col_change = directions[i // turn_every + 1]

            # Move the pointers
            a_row += a_row_change
            a_col += a_col_change
            b_row += b_row_change
            b_col += b_col_change

            i += 1
        
        self.rotate(matrix, layer+1)



'''
Transpose the matrix (reverse each diagonal, starting from top-left 'diagonal',
then the one underneath, and all others), then reverse each row. The diagonals
being reversed are the ones parallel to the diagonal that goes from the bottom-left
to the top-right corner. This results in a rotated image.
I wrote this solution after reading the editorial on LeetCode.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        '''
        A square has 2*N-1 diagonals.
        This function will reverse the first N diagonals,
        then the last N-1 diagonals.
        '''
        def transpose():
            # First N diagonals
            for d in range(N):
                ar, ac = d, 0
                br, bc = 0, d

                while ac < bc:  # can also use ar > br ?
                    # Swap
                    matrix[ar][ac], matrix[br][bc] = matrix[br][bc], matrix[ar][ac]

                    # Move a up-right and b down-left
                    ar, ac = ar-1, ac+1
                    br, bc = br+1, bc-1

            # Last N-1 diagonals
            for d in range(N-1):
                # a and b will initially be at the bottom-right corner
                ar, ac = N-1, N-1-d  # column will decrease with each iteration (going left)
                br, bc = N-1-d, N-1  # row will decrease with each iteration (going up)

                while ac < bc:
                    # Swap
                    matrix[ar][ac], matrix[br][bc] = matrix[br][bc], matrix[ar][ac]
                    
                    # Move a up-right and b down-left
                    ar, ac = ar-1, ac+1
                    br, bc = br+1, bc-1
        '''
        This function reverses each row, which "mirrors" the whole matrix
        '''
        def reverse():
            for r in range(N):
                for c in range(N//2):
                    matrix[r][c], matrix[r][N-1-c] = matrix[r][N-1-c], matrix[r][c]

        transpose()
        reverse()


'''
This is the same version as above, but written much more simply.
I wrote this after seeing the solution in the editorial on LeetCode.
'''
from itertools import product
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        '''
        Transpose:
        Traverse through the top-right triangle half of the square.
        For each spot (r,c), we swap it with (c,r).
        The main diagonal (top-left to bottom-right) isn't included.
        '''
        for r in range(N):
            for c in range(r+1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        '''
        Reverse:
        Swap each pair of elements, starting from the outermost elements
        and going inward until reaching the middle. Do this for all rows.
        '''
        for r in range(N):
            for c in range(N//2):
                matrix[r][c], matrix[r][N-1-c] = matrix[r][N-1-c], matrix[r][c]



        
        
        
        
