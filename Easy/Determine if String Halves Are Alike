//  https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution {
    public boolean halvesAreAlike(String s) {
        // Solved in 3 minutes 52 seconds
        
        int a = 0, b = 0;
        
        for(int i = 0; i < s.length()/2; i++)
            if(isVowel(s.charAt(i)))
                a++;
        
        for(int i = s.length()/2; i < s.length(); i++)
            if(isVowel(s.charAt(i)))
                b++;
        
        return a == b;
    }
    
    public boolean isVowel(char c) {
        return c == 'a' || c == 'e'  || c == 'i'  || c == 'o'  || c == 'u'  || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
}

/*
Sample input:
"book"
"ae"
"bookbeek"
"statestart"

*/
