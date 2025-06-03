/*
https://leetcode.com/problems/valid-number/
*/

class Solution {
    public boolean isNumber(String s) {
        boolean isValid = false;
        
        s = s.trim(); // trim extra spaces at the beginning and end of the string
        
        // edge case: an 'e' at the end does not cause the array to split the same way as for other 'e's
        if(s.length() == 0 || s.charAt(s.length() - 1) == 'e')
            return false;
        
        // check for an 'e'
        String[] splitE = s.split("e");
        
        // if there is an e present, the array should be size 2
        // if there isn't, the array should be size 1
        if(splitE.length == 2)
        {
            isValid = validLeft(splitE[0]) && validRight(splitE[1]);
        }
        else if(splitE.length == 1)
        {
            isValid = validLeft(splitE[0]);
        }
        else
        {
            return false;
        }
        
        return isValid;
    }
    
    // basically only accept if its a valid double
    // some forms it can take:
    // 2.9
    // +156.9
    // -67.9
    // 0
    // -0
    // +0
    // 3213
    // 99.4321
    public boolean validLeft(String str)
    {
        // Double.parseDouble() is smart enough to ignore spaces, so since there must be no spaces in this input
        // we need to turn them into 'x's (or anything else) so that they won't pass through Double.parseDouble()
        str = str.replace(" ", "x");
        
        // 'f's also pass through Double.parseDouble() (for ex. 900.94f is a valid java float), but we don't want them
        // so turn them into 'x's as well
        str = str.replace("f", "x");
        
        // same for 'D' and 'd' (a number like "12432143D" or "2147483648d" is accepted by parseDouble())
        str = str.replace("d","x");
        str = str.replace("D", "x");
        
        try {
            Double.parseDouble(str);
            return true;
        }
        catch(NumberFormatException ex)
        {
            return false;
        }
    }
    
    // basically only accept if its a valid int
    // some forms it can take:
    // +0
    // -0
    // 0
    // 13
    // +93
    // 342
    // -16
    public boolean validRight(String str)
    {
        try {
            Long.parseLong(str);
            return true;
        }
        catch(NumberFormatException ex)
        {
            return false;
        }
    }
}
