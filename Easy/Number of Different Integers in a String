//  https://leetcode.com/contest/weekly-contest-234/problems/number-of-different-integers-in-a-string/

class Solution {
    public int numDifferentIntegers(String word) {
        HashSet<String> nums = new HashSet<>();
        
        StringBuilder sb = new StringBuilder();
        
        char curChar;
        for(int i = 0; i < word.length(); i++) {
            curChar = word.charAt(i);
            if(Character.isDigit(curChar))
                sb.append(curChar);
            else {
                if(sb.length() > 0) { // if we have a number in there
                    nums.add(trim(sb.toString()));
                    sb = new StringBuilder();
                }
            }
        }
        
        if(sb.length() > 0) { // if we have a number in there
            nums.add(trim(sb.toString()));
            sb = new StringBuilder();
        }
        
        return nums.size();
    }
                     
     public String trim(String input) {
        int i = 0;
         while(i < input.length() && input.charAt(i) == '0')
             i++;
         
         if(i == input.length()) // if all #s were 0
             return "0";
         
         return input.substring(i);
     }
}

/*
Sample input:
"a123bc34d8ef34"
"01a001avs1dsafd1fdsaf0001"
"90fdsfads0090fdsf756adsaf00000000000000000090fdsa89"
"398271409832714039827410392847130294871039487103982714039841"
"000123412341234123413412dsfsdfds123412341234123413412jhfh"
"0a0"
"000a00b0fsafsd0000"
*/
