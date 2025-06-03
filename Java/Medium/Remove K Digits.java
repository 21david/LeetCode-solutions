/*
https://leetcode.com/explore/featured/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3328/

May Leetcoding challenge, day 13
*/
 /*
Approach:
If we remove k digits, then the resulting number will be an N digit number, where N = (nums.length() - k)
For that N digit number, there is a set of numbers that we can pick for the first number

Example:
1263105619, k = 5

for the leftmost digit, we can pick from:
1234560

for the next digit, we can pick from:
 2363105
 
then for the 3rd digit we can pick from:
  3631056
  
then ...
   6310561

then ...
    3105619

If we pick the smallest number at each stage, eliminating all numbers to the left when we do 
pick a number, then we should end up with the smallest possible number at the end.

5 ms, faster than 75.49%
*/
class Solution {
    public String removeKdigits(String nums, int k) {
        if(k == 0)
            return nums;
        
        if(nums.length() == k)
            return "0";
        
        boolean leadingZero = true;
        
        int[] digitsArray = new int[nums.length()];
        
        for(int i = 0; i < nums.length(); i++)
            digitsArray[i] = nums.charAt(i) - '0';
        
        StringBuilder sb = new StringBuilder();
        
        int min = 10;
        int minI = -1;
        
        try {
            for(int start = 0, end = k; start < end;  end++)
            {
                start = minI + 1;

                for(int i = start; i <= end; i++)
                {
                    if(digitsArray[i] < min)
                    {
                        min = digitsArray[i];
                        minI = i;
                    }
                }

                if(min != 0)
                    leadingZero = false;

                if(!leadingZero)
                    sb.append(min);

                min = 10;
            }
        }
        catch(ArrayIndexOutOfBoundsException ex) { }
                
        return (sb.length() == 0? "0" : sb.toString());
    }
}
