/*
https://leetcode.com/problems/divide-two-integers/
*/

/*
Four possible inputs, all have to be taken care of:
+, +
+, -
-, +
-, -
*/


class Solution {

    // legitimate solution    
    public int divide(int dividend, int divisor) {
        
        // Accepted
        // 1112 ms, faster than 13.03%
        // 36.9 mb, less than 6.06%
        
        if(dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        
        boolean neg1 = false, neg2 = false;
        
        if (divisor == 1)
        {
            return dividend;
        }
        
        if (divisor == -1)
        {
            return -dividend;
        }
        
        if(dividend < 0)
        {
            neg1 = true;
            dividend = -dividend;
        }
        if(divisor 
           < 0)
        {
            neg2 = true;
            divisor = -divisor;
        }
        
        int count = 0;
        
        while(dividend - divisor >= 0)
        {
            dividend -= divisor;
            count++;
        }
        
        
        if(neg1 && neg2) // both negative
            return count;
        else if(neg1 || neg2) // only one is negative
            return -count;
        else // both positive
            return count;    
    }
    
    
    // cheat solution
    public int divide2(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1)
                return Integer.MAX_VALUE;
        return dividend / divisor;   
    }
}
