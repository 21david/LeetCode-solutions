//  https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution {
    public int[] searchRange(int[] nums, int target) {
        // 0 ms, faster than 100%
        // 42.3 mb, less than 41.68%
        // Solved in 10 minutes
        
        /*
        We'll do a binary search to find the element.
        If not found, we return [-1,-1]. If found, we will
        make 2 pointers, one will try to travel left as far as it can,
        and the other one will travel right as far as it can.
        Then, we just return the indices of those pointers.
        
        */
        
        if(nums.length == 0)
            return new int[] {-1, -1};
        
        // binary search
        int lo = 0, hi = nums.length-1;
        int mid = 0;
        boolean found = false;
        
        while(lo <= hi) {
            mid = (lo + hi) / 2;
            
            if(nums[mid] == target) {
                found = true;
                break; // we found an index to work with
            }
            else if(nums[mid] < target)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        
        if(!found)
            return new int[] {-1, -1};
        
        // make 2 pointers and find the left and right indices
        int l = mid, r = mid;
        
        while(l-1 >= 0 && nums[l-1] == target)
            l--;
        
        while(r+1 < nums.length && nums[r+1] == target)
            r++;
        
        return new int[] {l, r};
    }
}

/*
Sample input:
[5,7,7,8,8,10]
8
[]
3
[1]
1
[2,2]
2
[3,3,3]
3
[4,4,4,4]
4
[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
1
[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
4
[1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
3
[1,1,2,2,3,3,4,4,5,5,7,7,8,8,9,9,10,10]
6
[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
1
[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7]
20
[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
9


*/
