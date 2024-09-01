/*
https://leetcode.com/problems/spiral-matrix/
*/

// Accepted
// 0 ms, faster than 100%
// 37.5 mb, less than 5.21%

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if(matrix == null || matrix.length == 0)
            return new ArrayList();
        
        int totalLength = matrix.length * matrix[0].length;
        int iterated = 0;
        
        ArrayList<Integer> ans = new ArrayList<>();
        boolean[][] visited = new boolean[matrix.length][matrix[0].length];
        
        int r = 0, c = 0;
        
        boolean canMove = true;
        
        // right, down, left, up
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int dir = 0;
        
        int dirR = 0;
        int dirC = 1;
        
        while(iterated < totalLength)
        {
            ans.add(matrix[r][c]);
                    
            visited[r][c] = true;
            
            // if it can't move in that direction
            if( !(inBounds(matrix, r + dirR, c + dirC) && !visited[r + dirR][c + dirC]) )
            {
                dir = (dir + 1) % 4; // then change direction   
                dirR = dirs[dir][0];
                dirC = dirs[dir][1];
            }
            
            // move in that direction
            r += dirR;
            c += dirC;
            
            iterated++;
        }
        
        return ans;
    }
    
    public boolean inBounds(int[][] matrix, int r, int c)
    {
        if(r < 0 || r >= matrix.length || c < 0 || c >= matrix[0].length)
            return false;
        else
            return true;
    }
}

// total time taken to solve: 59 mins
