/*
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3355/

June leetcoding challenge, day 9
*/

class Solution {
    public boolean isSubsequence(String s, String t) {
        // for each letter in s, iterate through t until it is found. If all are found, return true.
        
        int i = -1;
        int found = 0;
        
        for(char c : s.toCharArray())
        {
            i++;
            while(i < t.length() && t.charAt(i) != c)
                i++;
            
            if(i == t.length())
                return false;  // ran out of letters in t, with letters in s remaining
            
            found++;
        }
        
        return found == s.length();
    }
}
