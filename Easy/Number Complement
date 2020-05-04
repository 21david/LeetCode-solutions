/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3319/

May Leetcoding challenge, day 4
*/

class Solution {
    
    public int findComplement(int num) {
        // Accepted
        // 0 ms, faster than 100%
        // 36.5 mb, less than 8.70%
        
        // using bitwise operations
        
        int complement = 0;
        int bitTester = 1;
        
        while(bitTester <= num && bitTester >= 0)
        {
            if((num & bitTester) == 0)
                complement += bitTester;
            
            bitTester <<= 1;
        }
        
        return complement;
    }
    
    public int findComplement1(int N) {
        
        // solution from problem 1009: leetcode.com/problems/complement-of-base-10-integer
        
        // 1 ms, faster than 25%
        // 36.3 mb, less than 8.7%
        
        String nString = Integer.toBinaryString(N);
        
        int len = nString.length();
        
        String nFlipped = Integer.toBinaryString(~N); // flip all bits (will result in leading 1s because of two's complement reepresentation)
        
        String answerString = nFlipped.substring(nFlipped.length() - len); // remove the leading 1s
        
        int finalAnswer = Integer.parseInt(answerString, 2); // parse back into an integer
        
        return finalAnswer;
    }
    
    public int findComplement2(int num) {
        // Accepted
        // 0 ms, faster than 100%
        // 36.4 mb, less than 8.70%
        
        // using bitwise operations
        
        String bits = Integer.toBinaryString(num); // 7 -> "111"
        
        int complement = 0;
        int bitTester = 1;
        
        for(int i = 0; i < bits.length(); i++) // run once for each bit
        {
            if((num & bitTester) == 0)
                complement += bitTester;
            
            bitTester <<= 1;
        }
        
        return complement;
    }
    
    public int findComplement3(int num) {
        // Accepted
        // 11 ms, faster than 7.45%
        // 37.6 mb, less than 8.70%
        
        // using strings and Integer.toBinaryString()
        
        String bits = Integer.toBinaryString(num); // 7 -> "111"
        
        // flip all the bits
        // "111" -> "000"
        String complement = "";
        for(int i = 0; i < bits.length(); i++)
        {
            complement += bits.charAt(i) == '1' ? 0 : 1;
        }
        
        return Integer.parseInt(complement, 2);
    }
}
