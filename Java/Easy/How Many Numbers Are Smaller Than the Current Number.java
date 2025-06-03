//  https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        /*
        O(N*logN) approach:
        We can sort, by ascending.
        Then, for each number, if there it is repeated, then in the ascending list,
        we can move our pointer to the left as much as we can. Then, the index of this pointer
        is the number of numbers that this number is greater than.
        
        Example:
        [1, 2, 2, 3, 8]
            ^
        For the # 2, we move the pointer to index 1. This means that
        2 is only greater than 1 number. For every other number,
        the index it is in represents the amount of numbers that it is greater than.
        
        */
        
        int[] copy = nums.clone();
        int[] ans = new int[nums.length];
        
        HashMap<Integer, Integer> map = new HashMap<>();
        
        Arrays.sort(nums);
        
        for(int i = nums.length - 1; i >= 0; i--) {
            while(i > 0 && nums[i - 1] == nums[i])
                i--;
            
            // now map 8 with 4
            map.put(nums[i], i);
        }
        
        // now create the final array with the solution
        for(int i = 0; i < nums.length; i++) {
            ans[i] = map.get(copy[i]);
        }
        
        return ans;
    }
}
