/*
https://leetcode.com/problems/move-zeroes/
*/

// four solutions, each one is better than the one below it

class Solution {
    public void moveZeroes(int[] nums) {
        // Accepted
        // 0 ms, faster than 100%
        // 40.4 mb, less than 5.59%
        
        int i = 0;
        
        // iterate through every element only once
        for(int t = 0; t < nums.length; t++)
        {
            if(nums[t] != 0) // if non zero
            {
                // then swap with i, increasing i by 1 (for the next non-zero number)
                int temp = nums[t];
                nums[t] = nums[i];
                nums[i++] = temp;
            }
        }
    }
}


/*
class Solution {
    public void moveZeroes(int[] nums) {
        // Accepted
        // runtime is either 1 or 0 ms, different each time
        // if 0 ms, "faster than 100%""
        // if 1 ms, "faster than 17.70%"
        // 42.7 mb, less than 5.59%
        
        int i = 0;
        
        for(int t = 0; t < nums.length; t++)
            if(notZero(nums[t]))
                swap(nums, t, i++);
                
    }
    
    public boolean notZero(int val)
    {
        return val != 0;
    }
    
    public void swap(int[] nums, int val1, int val2)
    {
        int temp = nums[val1];
        nums[val1] = nums[val2];
        nums[val2] = temp;
    }
}
*/



/*
class Solution {
    public void moveZeroes(int[] nums) {
        // Accepted
        // 14 ms, faster than 5.15%
        // 42.5 mb, less than 5.59%
        
        boolean done = false;
        
        int indexOf0 = nums.length;
        int index = 0;
        
        //find the first 0
        for(int i = 0; i < nums.length; i++)
        {
            if(nums[i] == 0)
            {
                indexOf0 = i;
                break;
            }
        }
        
        // return if no 0s
        if(indexOf0 == nums.length)
            return;
        
        while(!done)
        {
            done = true;
        
            
            for(int i = indexOf0; i < nums.length; i++)
            {
                if(nums[i] != 0)
                {
                    index = i;
                    done = false;
                    break;
                }
            }
            
            if(done)
                return;
            
            // swap
            int temp = nums[index];
            nums[index] = nums[indexOf0];
            nums[indexOf0] = temp;
            
            indexOf0++;
        }
    }
}
*/

/*
class Solution {
    public void moveZeroes(int[] nums) {
        // Accepted
        // 40 ms, faster than 5.15%
        // 40.1 mb, less than 5.59%
        
        boolean found0 = false;
        boolean done = false;
        
        while(!done)
        {
            done = true;
            
            int indexOf0 = nums.length;
            int index = 0;
            
            for(int i = 0; i < nums.length; i++)
            {
                if(nums[i] == 0)
                {
                    indexOf0 = i;
                    break;
                }
            }
            
            for(int i = indexOf0 + 1; i < nums.length; i++)
            {
                if(nums[i] != 0)
                {
                    index = i;
                    done = false;
                    break;
                }
            }
            
            if(done)
                break;
            
            // swap
            int temp = nums[index];
            nums[index] = nums[indexOf0];
            nums[indexOf0] = temp;
        }
    }
}
*/
