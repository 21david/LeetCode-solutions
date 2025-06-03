//  https://leetcode.com/problems/max-area-of-island/submissions/

class Solution {
    int maxArea = 0;
    boolean[][] visited;
    int curArea = 0;
    
    public int maxAreaOfIsland(int[][] grid) {
        
        visited = new boolean[grid.length][grid[0].length];
        
        for(int r = 0; r < grid.length; r++) {
            for(int c = 0; c < grid[0].length; c++) {
                if(grid[r][c] == 1 && !visited[r][c])  { // found a new island, now find size 
                    explorer(grid, r, c);  // sets 'curArea' with the area of the current island
                    maxArea = Math.max(maxArea, curArea);
                    curArea = 0;
                }
            }
        }
        
        return maxArea;
    }
    
    public void explorer(int[][] grid, int r, int c) {
        // recursively travel in all 4 directions until whole island is marked as visited
        if(!inBounds(grid, r, c) || visited[r][c])  // ignore all out of bounds or already visited locations
            return;
        
        if(grid[r][c] != 1)  // ignore water
            return;
        
        visited[r][c] = true;
        curArea++;
        
        explorer(grid, r-1, c);
        explorer(grid, r+1, c);
        explorer(grid, r, c-1);
        explorer(grid, r, c+1);
    }
    
    public boolean inBounds(int[][] grid, int r, int c) {
        return !(r < 0 || c < 0 || r >= grid.length || c >= grid[0].length);
    }
}
