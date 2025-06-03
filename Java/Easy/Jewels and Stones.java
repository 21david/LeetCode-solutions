/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/

May 30-day LeetCoding, day 2
*/

class Solution {
    
    public int numJewelsInStones7(String J, String S) {
        // faster than 80.93%
        
        // O(J + S)
        HashSet<Character> jewels = new HashSet<>();
        
        for(char j : J.toCharArray())
            jewels.add(j);
        
        int count = 0;
        
        for(char s : S.toCharArray())
            if(jewels.contains(s))
                count++;
        
        return count;
    }
    
    public int numJewelsInStones(String J, String S) {
        // faster than 100%
        // interesting, despite worse runtime
        
        // O(J * S)
        int count = 0;
        
        for(char c : S.toCharArray())
            if(J.indexOf(c) >= 0)
                count++;
        
        return count;
    }
}
