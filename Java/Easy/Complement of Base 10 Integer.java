/*
https://leetcode.com/problems/complement-of-base-10-integer/

This problem is the same as #476:   leetcode.com/problems/number-complement
See my solutions for that one:   github.com/21david/More-LeetCode-problems/blob/master/Easy/Number%20Complement

1 ms, faster than 27.31%
35.9 mb, less than 11.11%
*/
class Solution {
    public int bitwiseComplement(int N) {
        String nString = Integer.toBinaryString(N);
        
        int len = nString.length();
        
        String nFlipped = Integer.toBinaryString(~N); // flip all bits (will result in leading 1s because of two's complement reepresentation)
        
        String answerString = nFlipped.substring(nFlipped.length() - len); // remove the leading 1s
        
        int finalAnswer = Integer.parseInt(answerString, 2); // parse back into an integer
        
        return finalAnswer;
    }
}
