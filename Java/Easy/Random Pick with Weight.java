/*
https://leetcode.com/explore/featured/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3351/

June leetcoding challenge, day 5
*/

class Solution {
    private int[] w;
    private int[] intervals;
    private int totalSum;
    
    public Solution(int[] w) {
        this.w = w;
        intervals = new int[w.length + 1];
        
        int sum = 0;
        
        for(int i = 1; i < intervals.length; i++)
        {
            sum += w[i-1];
            intervals[i] = sum;
        }
        
        totalSum = sum;
        
        System.out.println(Arrays.toString(intervals));
    }
    
    public int pickIndex() {
        int randNum = (int) (Math.random() * totalSum);
        
        for(int i = 0; i < intervals.length - 1; i++)
            if(randNum >= intervals[i] && randNum < intervals[i + 1])
                return i;
        
        return -1;  // code should never reach this point
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
