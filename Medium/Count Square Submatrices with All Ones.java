/*
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/536/week-3-may-15th-may-21st/3336/

May Leetcoding challenge, day 21
*/

class Solution {
    public int countSquares(int[][] matrix)
    {
        // 8 ms, faster than 29.87%
        // 49.2 mb, less than 100%
        
        // time complexity: O(M * N)
    
        int count = 0;

        // this uses DP
        for(int i = 0; i < matrix.length; i++)
        {
            for(int j = 0; j < matrix[0].length; j++)
            {
                if(i != 0 && j != 0 && matrix[i][j] == 1)
                    matrix[i][j] = min( matrix[i-1][j-1],  matrix[i-1][j],  matrix[i][j-1] )  + 1;
                
                count += matrix[i][j];
            }
        }

        return count;
    }
    
    
    // returns the min out of a list of integers
    public int min(int... nums) 
    {
        int min = nums[0];
        
        for(int i = 1; i < nums.length; i++)
            if(nums[i] < min)
                min = nums[i];
        
        return min;
    }
}
