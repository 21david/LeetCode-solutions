//  https://leetcode.com/problems/beautiful-arrangement-ii/

class Solution {
    public int[] constructArray(int n, int k) {
        // 0 ms, faster than 100%
        // 39.4 mb, less than 44.57%
        // Solved in 34 minutes (used expected output as a hint of sorts)
        
        /*
        A pattern that seems to work is: if we want k distinct differences,
        then we can start with 1, add k to get the second element,
        subtract (k-1) from the second element to get the third element,
        add (k-2) from the third element to get the fourth element, 
        until we add or subtract 1. Then, if there are any remaining elements,
        (from the set {1, 2, ..., n}) we just add them to the end in sequential order.
        
        This would be a greedy algorithm to solve the problem.
        
        Runtime: O(N)
        Space complexity: O(N)
        */
        
        int kOriginal = k;
        
        int[] ans = new int[n];
        ans[0] = 1;
        
        // we will alternate between adding and subtracting the value of k
        // subtracting 1 from its value each time
        for(int i = 1; i <= kOriginal; i++) {
            if(i%2 == 1) {
                ans[i] = ans[i-1] + k;
            }
            else {
                ans[i] = ans[i-1] - k;
            }
            
            k--;
        }
        
        // fill in the rest of the array
        for(int i = kOriginal + 1; i < ans.length; i++) {
            ans[i] = i+1;
        }
        
        return ans;
    }
}
