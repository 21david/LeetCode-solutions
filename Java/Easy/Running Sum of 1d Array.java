//  https://leetcode.com/problems/running-sum-of-1d-array/

class Solution {
    
    public int[] runningSum2(int[] nums) {
        // 0 ms, faster than 100%
        // 39 mb, less than 70.13%  (varies for every submission)
        // this one has O(1) space complexity instead of O(N)
        // both have O(N) time complexity
        
        for(int i = 1; i < nums.length; i++)
            nums[i] += nums[i-1];
        
        return nums;
    }
    
    public int[] runningSum2(int[] nums) {
        // 0 ms, faster than 100%
        // 38.9 mb, less than 83.04%  (varies for every submission)
        // Solved in 1 minute 24 seconds
        
        int sum = nums[0];
        
        int[] sol = new int[nums.length];
        sol[0] = sum;
        
        for(int i = 1; i < nums.length; i++) {
            sum += nums[i];
            sol[i] = sum;
        }
        
        return sol;
    }
}
