//  https://leetcode.com/contest/weekly-contest-234/problems/minimum-number-of-operations-to-reinitialize-a-permutation/
//  (Need a LeetCode account to see ^)

class Solution {
    public int reinitializePermutation(int n) {
        int[] perm = new int[n];
        for(int i = 0; i < perm.length; i++)
            perm[i] = i;
        
        int[] newIndices = new int[n];
        for(int i = 0; i < newIndices.length; i++) {
            if(i % 2 == 0) {  // even indices
                newIndices[i] = perm[i / 2];
            }
            else {  // odd indices
                newIndices[i] = perm[n / 2 + (i - 1) / 2];
            }
        }
        
        int[] result = new int[n];
        for(int i = 0; i < perm.length; i++) {
            result[i] = perm[newIndices[i]];
        }
        
        int count = 1;
        
        while(!isOriginal(result)) {
            // copy result onto perm, and start over
            for(int i = 0; i < result.length; i++)
                perm[i] = result[i];
            
            for(int i = 0; i < perm.length; i++) {
                result[i] = perm[newIndices[i]];
            }
            count++;
        }
        
        return count;
    }
    
    // It's "original" if its [0, 1, 2, 3, ..., length - 1]
    public boolean isOriginal(int[] array) {
        for(int i = 0; i < array.length; i++)
            if(array[i] != i)
                return false;
        
        return true;
    }
}
