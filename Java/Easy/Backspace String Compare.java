/*
https://leetcode.com/problems/backspace-string-compare/
*/

// LeetCode 30 day challenge, day 9
// Accepted
// 3 ms, faster than 15.19%
// 37.8 mb, less than 6.06%
class Solution {
    public boolean backspaceCompare(String S, String T) {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        
        // skip all beginning #s
        int i = 0;
        
        while(i < S.length() && S.charAt(i) == '#')
            i++;
        
        // i should be on the first non-# in S
        
        // skip all beginning #s
        int j = 0;
        
        while(j < T.length() && T.charAt(j) == '#')
            j++;
        
        // j should be on the first non-# in T
        
        while(i < S.length())
        {
            if(S.charAt(i) == '#')
            {
                if(sb1.length() >= 1)
                    sb1.deleteCharAt(sb1.length() - 1);
            }
            else
                sb1.append(S.charAt(i));
            
            i++;
        }
        
        while(j < T.length())
        {
            if(T.charAt(j) == '#')
            {
                if(sb2.length() >= 1)
                    sb2.deleteCharAt(sb2.length() - 1);
            }
            else
                sb2.append(T.charAt(j));
            
            j++;
        }
        
        return sb1.toString().equals(sb2.toString());
    }
}
