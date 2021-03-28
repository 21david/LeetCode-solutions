//  https://leetcode.com/problems/find-pivot-index/

class Solution {
    public int pivotIndex(int[] nums) {
        // 2 ms, faster than 30.03%
        // 39.7 mb, less than 57.24%
        // Solved in 9 minutes
        
        /*
        O(N) solution by finding the sum of the array, 
        then starting from the left, subtract nums[i] from the sum
        and add it to another sum. Repeat this until both sums
        are equal, or if they never are, until the end
        
        */
        
        int sum = 0;
        
        for(int n : nums)
            sum += n;
        
        if(sum - nums[0] == 0)
            return 0;
        
        int sumLeft = 0;
        
        for(int i = 0; i < nums.length - 1; i++) {
            sumLeft += nums[i];
            sum -= nums[i];
            sum -= nums[i+1];
            
            if(sumLeft == sum)
                return i+1;
            
            sum += nums[i+1];
        }
        
        return -1;
    }
}
/*
Sample input:
[1,7,3,6,5,6]
[2,1,-1]

*/
