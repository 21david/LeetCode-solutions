/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

May Leetcoding challenge, day 11
*/

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        
        // 0 ms, faster than 100%
        // 40.3 mb, less than 89.47%
        
        /*
        Flood fill algorithm:
        Keep the original value of image[sr][sc] stored in a temp variable.
        Recursively go up, down left, right, starting from image[sr][sc]
          - if the new location == original value, change it to new value
          - if it is equal to anything else, don't make further recursive calls
          
        */
          
        int originalVal = image[sr][sc];
        
        if(originalVal == newColor)
            return image; // flood filling would make no change (and would result in infinite loop)
        
        floodFill(image, originalVal, newColor, sr, sc);
        
        return image;
    }
    
    
    public void floodFill(int[][] image, int originalVal, int newVal, int r, int c)
    {
        if(outOfBounds(image, r, c))
            return;
        
        if(image[r][c] == originalVal)
        {
            image[r][c] = newVal;
            
            floodFill(image, originalVal, newVal, r + 1, c);
            floodFill(image, originalVal, newVal, r - 1, c);
            floodFill(image, originalVal, newVal, r, c + 1);
            floodFill(image, originalVal, newVal, r, c - 1);
        }
    }
    
    public boolean outOfBounds(int[][] image, int r, int c)
    {
        return r < 0 || c < 0 || r >= image.length || c >= image[0].length;
    }
}
