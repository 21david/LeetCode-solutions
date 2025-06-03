//  https://leetcode.com/problems/missing-number-in-arithmetic-progression/

class Solution {
    public int missingNumber(int[] arr) {
        // 0 ms, faster than 100%
        // 38.2 mb, less than 94.80%
        // Solved in 16 minutes 45 seconds
        
        /*
        We can find the value arr[i+1] - arr[i] is supposed to be
        by subtracting, and keeping the first value that happens twice.
        Then, we can find the index i such that arr[i+1] != arr[i],
        and use that to find the missing number.
        
        */
        
        int diff1 = arr[1] - arr[0];
        int diff2 = arr[2] - arr[1];
        
        int officialDiff;
        
        // using just the first 2 differences, we should be able to find
        // the common difference that is being used in the sequence
        if(diff1 == diff2)
            officialDiff = diff1;
        else {
            if(diff1 > 0)
                officialDiff = Math.min(diff1, diff2);
            else
                officialDiff = Math.min(Math.abs(diff1), Math.abs(diff2)) * -1;
        }
        
        if(officialDiff == 0)
            return arr[0];
        
        // now we know the common difference that is being used,
        // we have to find where that common difference isn't being used
        for(int i = 0; i < arr.length - 1; i++) {
            if(arr[i+1] - arr[i] != officialDiff) {
                // from here, we can find the missing number
                // by adding the officialDiff to the first number
                return arr[i] + officialDiff;
            }
        }
        
        return -1;
    }
}

/*
Sample input:
[5,7,11,13]
[0,0,0,0,0,0,0]
[100,100,100]
[1,5,13,17]
[1,9,13,17]
[1,5,13,17,21,25,29,33,37,41]
[21,13,9,5,1]
[21,17,9,5,1]

*/
