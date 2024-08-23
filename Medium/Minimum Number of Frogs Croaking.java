/*
https://leetcode.com/problems/minimum-number-of-frogs-croaking/

Weekly Contest 185, problem 3
*/

class Solution {
    public int minNumberOfFrogs(String croakOfFrogs) {
        int[] croak = new int[5];
        int croaksStarted = 0;
        int min = 1;
        
        for(char c : croakOfFrogs.toCharArray())
        {
            switch(c)
            {
                case 'c':
                    croak[0]++;
                    croaksStarted++;
                    min = Math.max(min, croaksStarted);
                    break;
                
                case 'r':
                    if(croak[0] >= 1)
                    {
                        min = Math.max(min, croak[0]);
                        croak[0]--;
                        croak[1]++;
                    }
                    else // an r without a preceding c
                    {
                        return -1;
                    }
                    break;
                    
                case 'o':
                    if(croak[1] >= 1)
                    {
                        min = Math.max(min, croak[0]);
                        croak[1]--;
                        croak[2]++;
                    }
                    else // an o without a preceding r
                    {
                        return -1;
                    }
                    break;
                    
                case 'a':
                    if(croak[2] >= 1)
                    {
                        min = Math.max(min, croak[0]);
                        croak[2]--;
                        croak[3]++;
                    }
                    else // an a without a preceding o
                    {
                        return -1;
                    }
                    break;
                    
                case 'k':
                    if(croak[3] >= 1)
                    {
                        min = Math.max(min, croak[0]);
                        croaksStarted--;
                        croak[3]--;
                        croak[4]++;
                    }
                    else // a k without a preceding a
                    {
                        return -1;
                    }
                    break;
                    
                default: // if it was a letter other than one in "croak"
                    return -1;
            }
            
        }
        
        // if at the end the array looks anything like: [0, 0, 0, 0, X]
        // then it was invalid input
        
        for(int i = 0; i <= 3; i++)
            if(croak[i] != 0)
                return -1;
        
        if(croak[4] <= 0)
            return -1;
        
        return min;
    }
}
