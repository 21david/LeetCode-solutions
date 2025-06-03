//  https://leetcode.com/problems/longest-valid-parentheses/

/*
We can use the normal algorithm that checks whether a string of parenthesis is 
valid, but with a few changes. We can make a boolean array the same size of the
input string, and initially set all elements to false. We can make a stack that will
store '('s, and another stack that stores the index of all the '('s we find. Whenever
we find a ')' with a matching '(' in the stack, then we know the index of both the
'(' and ')' because of the other stack we have. In the boolean array, we can set both
the element at those indices to true. This will be an O(N) operation.
At the end, we will have a boolean array that knows all of the valid parenthesis and 
all of the invalid parenthesis. We can iterate through this array, keeping track of the
lengths of the valid substrings, and looking out for the maximum length one. This is
O(N) again.

2 ms, faster than 68.47%
38.9 mb, less tan 56.64%
Solved in ~30 minutes
*/
class Solution {
    public int longestValidParentheses(String s) {
        boolean[] validOrNot = new boolean[s.length()];
        Arrays.fill(validOrNot, false);
        
        int parenthesis = 0;
        Stack<Integer> indices = new Stack<>();
        
        char curChar;
        int index;
        for(int i = 0; i < s.length(); i++) {
            curChar = s.charAt(i);
            
            if(curChar == '(') {
                parenthesis++;
                indices.push(i);
            }
            else {
                if(parenthesis == 0)
                    continue;
                
                // if it's not empty, and there is a matching '(', then
                parenthesis--;
                index = indices.pop();
                
                // now we have the indices of two matching parenthesis
                validOrNot[index] = true;
                validOrNot[i] = true;
            }
        }
        
        // now we have to find the largest amount of consecutive 'true's in the boolean array
        int max = 0;
        int curInterval = 0;
        for(int i = 0; i < validOrNot.length; i++) {
            if(validOrNot[i] == false) {
                curInterval = 0;
            }
            else {
                curInterval++;
                max = Math.max(max, curInterval);
            }
        }
        
        return max;
    }
}

/*
Sample input:
""
"("
")"
")))"
"(()"
"()()"
"())("
")()())(()()())("
")()((())("
*/
