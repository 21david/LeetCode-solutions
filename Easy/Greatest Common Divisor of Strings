//  https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution {
    public String gcdOfStrings(String str1, String str2) {
        // 100 ms, faster than 5.07%
        // 104.1 mb, less than 5.21%
        
        /* 
            Find the longest substring that the two strings have in common, 
             starting from the first letter.
            Using this substring, check if it can be concatenated with 
             itself to create the input strings
            If it can, return it. If not, take a letter off from the end
             of this substring and try it again.
            If it never finds the solution, return empty string at the end.
       */
        
        // find the longest common prefix between the two strings (the most amount of letters
        // that both strings have in common in the beginning)
        int i = 0;
        StringBuffer commonPrefix = new StringBuffer();
        while(i < str1.length() && i < str2.length() && str1.charAt(i) == str2.charAt(i))
            commonPrefix.append(str1.charAt(i++));
        
        // if nothing in common, then there is no solution string
        if(i == 0)
            return "";
        
        // use this prefix to try to construct both the input strings
        // if they can't be constructed, then try again but with 1 less letter off the end
        
        for(int a = commonPrefix.length(); a > 0; a--) {
            StringBuffer substr = new StringBuffer(commonPrefix.substring(0, a));
            StringBuffer sb1 = new StringBuffer(commonPrefix.substring(0, a));
            StringBuffer sb2 = new StringBuffer(commonPrefix.substring(0, a));
            
            // concatenate sb1 with itself until it is >= length of original str1
            while(sb1.length() < str1.length())
                sb1.append(substr);
            
            // concatenate sb2 with itself until it is >= length of original str2
            while(sb2.length() < str2.length())
                sb2.append(substr);
            
            // if they constructed the original strings perfectly, return this as the solution
            if(sb1.toString().equals(str1) && sb2.toString().equals(str2))
                return substr.toString();
                
        }
        
        // if a string was never found, not even of length 1, then there is no solution
        return "";
    }
}

/*

Test cases:

"ABCABC"
"ABC"
"ABABAB"
"ABAB"
"LEET"
"CODE"
"ABCDEF"
"ABC"
"ABCABCABCABCABCABC"
"ABCABC"
"AAAAAAAAA"
"AAACCC"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

*/
