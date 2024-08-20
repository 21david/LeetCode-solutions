//  https://leetcode.com/problems/jump-game/

class Solution {
    public boolean canJump(int[] nums) {
        // 236 ms, faster than 32.03%
        // 42.6 mb, less than 17.16%
        
        /*
        Possible approach:
        Start from the end, and figure out the left-most element that can reach the end. This will be
        the last jump. Then, repeat, but pretend that that value you found is now the end of the array.
        Repeat this until the first element is reached, or until a spot cannot be found. Technically, this could be done recursively.
        
        I think this is O(N^2) time complexity approach (for example, an array of all 1s would cause O(N^2) behavior)
        Space complexity is O(1)
        */
        
        return findFurthestElement(nums, nums.length - 1);
    }
    
    public boolean findFurthestElement(int[] nums, int curEndIndex) {
        if(curEndIndex == 0)
            return true;
        
        // curIndex will start at the end of the array
        // so we have to find the leftmost element that can jump to curIndex
        
        int indexThatCanJump = curEndIndex;
        int jumpLength = 1;
        boolean found = false;
        for(int i = curEndIndex - 1; i >= 0; i--) {
            if(nums[i] >= jumpLength) {  // if this element can jump to the end
                indexThatCanJump = i;  // save this element
                found = true;
            }
            jumpLength++;
        }
        
        // if we never found a spot that can jump, then answer is false
        if(!found)
            return false;
        
        // now we should do it again, but starting from whatever index we found (indexThatCanJump)
        return findFurthestElement(nums, indexThatCanJump);
    }
}

/*
Sample input:
[0]
[2]
[2,3,1,1,4]
[2,3,0,1,4]
[3,5,1,1,1,1,6,1,1,1,1,1]
[2,0,0,3,5,1,1,1,1,6,1,1,1,1,1]
[6,1,1,1,4,2,1,1,6,4,3,2,1,1]
[1,0,6,1,1,1,4,2,1,1,6,4,3,2,1,1]

*/
