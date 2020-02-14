/*
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
*/

// done through webcam with Leah

class Solution {
    public int dominantIndex(int[] nums) {
        // find the maximum element
        
        int max = nums[0];
        int maxIndex = 0;
        
        for(int i = 1; i < nums.length; i++)
        {
            if(nums[i] > max)
            {
                max = nums[i];
                maxIndex = i;
            }
        }
        
   //     System.out.println(max + " " + maxIndex);
        
        // iterate through numbers, looking for a counterexample
        for(int i = 0; i < nums.length; i++)
        {
            if(maxIndex == i) // skip the largest element itself
                continue;
            
            if(nums[i] > max / 2) // if it finds a fault, return -1
                return -1;
        }
        
        return maxIndex;
    }
}
