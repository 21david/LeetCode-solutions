/*
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3318/

May LeetCoding Challenge, day 3
*/

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        // O(N)
        // faster than 98.69%
        
        if (magazine.length() < ransomNote.length())
            return false;
        
        int[] alphabet1 = new int[26];
        int[] alphabet2 = new int[26];
        
        for(char c : ransomNote.toCharArray())
            alphabet1[c-'a']++;
        
        for(char c : magazine.toCharArray())
            alphabet2[c-'a']++;
        
        // each letter in alphabet1 has to have at least the same amount in alphabet2
        
        for(int i = 0; i < 26; i++)
            if(alphabet1[i] > alphabet2[i])
                return false;
        
        return true;
    }
}
