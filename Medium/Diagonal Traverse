//  https://leetcode.com/problems/diagonal-traverse/

class Solution {
    
    int[] answer;
    int a = 0;
    
    int row = 0, col = 0;
    int count = 0;
    
    public int[] findDiagonalOrder(int[][] matrix) {
        // 2 ms, faster than 90.72%
        // 41.2 mb, less than 39.69%
        
        /*
        Inspired by solution #2 on LeetCode. 
        We can use the tail of the previous diagonal (the position of the last element
        that was visited) to determine the head of the next diagonal (the position of the
        first element we will traverse). If we went upwards and to the right, the next head
        will either be to the right, or directly below. If we went downards and to the left,
        the next head will either be directly below or to the right
        */
        
        if(matrix.length == 0 || matrix[0].length == 0)
            return new int[0];
        
        int numOfElements = matrix.length * matrix[0].length;
        
        // initialize final array that stores answer
        answer = new int[numOfElements];
        
        int diagonal = 0; // used to switch diagonal directions
        
        while(count < numOfElements) {
            
            if(diagonal % 2 == 0)  // upwards diagonal
                upRight(matrix);
            else  // downwards diagonal
                downLeft(matrix);
            
            // after the diagonal's traverse, find the next head
            
            if(diagonal % 2 == 0) { // if we traveled upwards
                // then the next head will either be to the right, or below
                if(!outOfBounds(matrix, row, col + 1)) // check spot to the right
                    col++; // go to the right
                else
                    row++; // go below
            }
            else {
                // then the next head will either be below, or to the right
                if(!outOfBounds(matrix, row + 1, col)) // check spot below
                    row++; // go below
                else
                    col++; // go to the right
            }
            
            diagonal++;
        }
        
        return answer;
    }
    
    // starting at matrix[row][col], traverse it in a diagonal going up-right, and add the elements to result
    public void upRight(int[][] matrix) {
        if(outOfBounds(matrix, row, col)) // then we reached the tail
        {
            // move it back from an out of bounds position
            row++;
            col--;
            
            return;
        }
        
        count++;
        answer[a++] = matrix[row][col];
        
        // move current position up-right
        row--;
        col++;
        
        upRight(matrix);
    }
    
    // starting at matrix[row][col], traverse it in a diagonal going down-left, and add the elements to result
    public void downLeft(int[][] matrix) {
        if(outOfBounds(matrix, row, col))
        {
            // move it back from an out of bounds position
            row--;
            col++;
            
            return;
        }
        
        count++;
        answer[a++] = matrix[row][col];
        
        // move current position up-right
        row++;
        col--;
        
        downLeft(matrix);
    }
    
    public boolean outOfBounds(int[][] matrix, int r, int c) {
        return r < 0 || c < 0 || r >= matrix.length || c >= matrix[0].length;
    }
}
