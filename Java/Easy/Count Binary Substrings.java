//  https://leetcode.com/problems/count-binary-substrings/

/*
Inspired by the solution:
Turn the input string into an array of ints, where each int
in the array represents the length of a substring of consecutive 1s or 0s.
So "000110000001111111111" would become [3, 2, 6, 10]
After this, for every pair of adjacent ints in the array, we can
determine how many substrings we can count. For example, 
with 3 and 2, we know it will be "11100" or "00111", and in both
cases, we can form 2 substrings (which is min(3, 2)). So for all pairs,
we add min(arr[i], arr[i+1]) to a counter variable, and return
the value of that variable at the end.    

10 ms, faster than 20.55%
39.6 mb, less than 12.32%
*/
class Solution {
    public int countBinarySubstrings(String s) {
        ArrayList<Integer> array = new ArrayList<>();
        
        char num = s.charAt(0);
        int size = 1;
        char temp;
        
        loop:
        for(int i = 1; i <= s.length(); i++) {
            size = 1;
            
            if(i >= s.length()) {
                array.add(size);
                break loop;
            }
            
            temp = s.charAt(i);
            while(temp == num) {
                size++;
                i++;
                
                if(i >= s.length()) {
                    array.add(size);
                    break loop;
                }
                temp = s.charAt(i);
            }
            num = temp;  // at this point, it switches digits (0 to 1, or 1 to 0)
            array.add(size);
        }
        
        int count = 0;
        
        for(int i = 0; i < array.size() - 1; i++) {
            count += Math.min(array.get(i), array.get(i+1));    
        }
        
        return count;
    }
    

/*
A brute force approach would be to check all substrings of size 2, then size 3,
until the subtring reaches the size of the whole string. I think this would be
O(N^2) complexity, which would probably not pass the time limit.

Another approach would be to check all substrings of size 2, and when a substring
that matches the pattern is found, store the index of that substring somewhere.
Once the whole string is iterated through, we should have a list of all the size 2
substrings that match, and any other substrings that match will start from these.
So, for each substring of size 2, we can try to expand as much as we can, counting any
new substrings that we find. Once we've tried all the substrings, we should have
a count of all the substrings (of all sizes) that match the pattern in the description.

19 ms, faster than 5.58%
40 mb, less than 7.16%
Solved in 32 minutes 30 seconds
*/
public int countBinarySubstrings2(String s) {
        ArrayList<Integer> indices = new ArrayList<>();
        
        // iterate through string, finding substrings of size 2 that look like "01" or "10"
        for(int i = 0; i < s.length() - 1; i++) {
            if((s.charAt(i) == '0' && s.charAt(i+1) == '1') || (s.charAt(i) == '1' && s.charAt(i+1) == '0'))
                indices.add(i);
        }
        
        // any substring that we already found will count towards the solution
        int count = indices.size();
        
        // now we have to try to expand from the ones we found to find bigger ones
        int rightIndex;
        char leftNum, rightNum;
        for(int leftIndex : indices) {
            rightIndex = leftIndex+1;
            
            leftNum = s.charAt(leftIndex); // either a 1 or a 0
            rightNum = s.charAt(rightIndex); // opposite number from leftNum
            
            // try to expand
            leftIndex--;
            rightIndex++;

            // while both pointers are still within bound
            while(leftIndex >= 0 && rightIndex < s.length()) {

                if(s.charAt(leftIndex) == leftNum && s.charAt(rightIndex) == rightNum)  // if still a match
                    count++;
                else
                    break;
                
                // try to expand
                leftIndex--;
                rightIndex++;
            }
        }
        
        return count;
    }
}

/*
Sample input:
"01"
"10"
"0101"
"1010"
"01010"
"010101"
"0101010"
"01010101"
"010101010101010101010101"
"101010101010101010101010"
"00110"
"00110011"
"0000001111110011"
"00001111001100000000001111111111111000111000"

*/
