//  https://leetcode.com/problems/jump-game-ii/

class Solution {
    public int jump(int[] nums) {
        // 0 ms, faster than 100%
        // 36.4 mb, less than 42.70%
        // Solved in 27 minutes
        
        /*
        Possible approach:
        Start from the end, and figure out the left-most element that can reach the end. This will be
        the last jump. Then, repeat, but pretend that that value you found is now the end of the array.
        Repeat this until the first element is reached. Technically, this could be done recursively.
        
        I think this is O(N^2) time complexity approach (for example, an array of all 1s would cause O(N^2) behavior)
        Space complexity is O(1)
        */
        
        findFurthestElement(nums, nums.length - 1);
        return jumps;
    }
    
    private int jumps = 0;
    
    public void findFurthestElement(int[] nums, int curEndIndex) {
        if(curEndIndex == 0)
            return;
        
        // curIndex will start at the end of the array
        // so we have to find the leftmost element that can jump to curIndex
        
        int indexThatCanJump = curEndIndex;
        int jumpLength = 1;
        for(int i = curEndIndex - 1; i >= 0; i--) {
            if(nums[i] >= jumpLength)  // if this element can jump to the end
                indexThatCanJump = i;  // save this element
            jumpLength++;
        }
        
        // after 1 iteration, we should have found a jump
        jumps++;
        
        // now we should do it again, but starting from whatever index we found (indexThatCanJump)
        findFurthestElement(nums, indexThatCanJump);
    }
}

/*
Sample input:
[2,3,1,1,4]
[2,3,0,1,4]
[3,5,1,1,1,1,6,1,1,1,1,1]
[6,1,1,1,4,2,1,1,6,4,3,2,1,1]

*/
