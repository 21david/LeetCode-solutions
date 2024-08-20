// https://leetcode.com/problems/count-number-of-teams/

class Solution {
    public int numTeams(int[] rating) {
        /*
        A brute force approach, which may work since n <= 200, would be to
        have three pointers that change positions to check all the possible
        combinations of teams, given the conditions for i, j, k.
        For each possibility, if it matches the conditions, then we add 1 to
        a counter variable.
        
        To iterate through the possibilities, we can set i, j, k to 0, 1, 2,
        and iterate k until the end of the list. Then, we can increment j, set k to
        j + 1, and repeat. We repeat this until j and k reach the last 2 spots in the list.
        Then, we increment i and repeat the process.
        
        */
        
        // count the # of teams we can form
        int count = 0;
        
        // set up pointers
        int i = 0, j = 1, k = 2;
        
        // iterate pointers through every possibility
        // if the pointers form a valid team, add 1 to 'count'
        while(i < rating.length - 2) {
            while(j < rating.length - 1) {
                while(k < rating.length) {
                    if(checkTeam(rating, i, j, k)) // if this is a valid team
                        count++;
                    
                    k++;
                }
                
                j++;
                k = j + 1;
            }
            
            i++;
            j = i + 1;
            k = j + 1;
        }
        
        return count;
    }
    
    /*
    Check if the soldiers represented by the pointers form a valid team.
    (That is, rating[i] < rating[j] < rating[k] OR rating[i] > rating[j] > rating[k])
    */
    public boolean checkTeam(int[] rating, int i, int j, int k) {
        return (rating[i] < rating[j] && rating[j] < rating[k]) 
            || (rating[i] > rating[j] && rating[j] > rating[k]);
    }
}
