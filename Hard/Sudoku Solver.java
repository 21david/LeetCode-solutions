//  https://leetcode.com/problems/sudoku-solver/
// 7 ms, faster than 79.20%
// 37 MB, less than 45.61%

class Solution {
    public void solveSudoku(char[][] board) {
    	solveSudokuHelp(board);
    }
    
    public boolean solveSudokuHelp(char[][] board) {
    	// iterate through every cell
    	for(int r = 0; r < 9; r++) {
    		for(int c = 0; c < 9; c++) {
    			if(board[r][c] != '.')  // skip if its a number
    				continue;
    			
    			// if its an open cell, try all nums
    			for(int i = 1; i <= 9; i++) {
    				// if this num doesn't break the board
    				if(!breaksBoard(board, r, c, i)) {
    					board[r][c] = (char) ('0' + i);
                        
    					if(solveSudokuHelp(board))
    						return true;
    					
    					board[r][c] = '.';
    				}
    			}
    			
    			return false;
    		}
    	}
    	
    	return true;
    }
    
	// if num is already present in the row, col, or subgrid, then it breaks the board
    private boolean breaksBoard(char[][] board, int r, int c, int n) {
    	char num = (char) (n + '0');
    	
    	// check the row
    	for(int i = 0; i < 9; i++)
    		if(board[r][i] == num)
    			return true;
    	
    	// check the col
    	for(int i = 0; i < 9; i++)
    		if(board[i][c] == num)
    			return true;
    	
        // check  all 9 squares in the subgrid it's in
    	int subgridR = r / 3;
    	int subgridC = c / 3;
    	
    	for(int i = subgridR * 3; i < subgridR * 3 + 3; i++)
    		for(int j = subgridC * 3; j < subgridC * 3 + 3; j++)
    			if(board[i][j] == num)
    				return true;
    	
    	return false;
    }
}
