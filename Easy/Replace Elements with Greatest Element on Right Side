//  https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution {
    public int[] replaceElements(int[] arr) {
        // 1 ms, faster than 99.76%
        // 40.5 mb, less than 33.8%
        
        // time complexity: O(N)
        // space complexity: O(1)
        
        int curMax1 = -1;
        int curMax2 = -1;
        
        for(int i = arr.length - 1; i >= 0; i--) {
            curMax1 = Math.max(curMax1, arr[i]);
            arr[i] = curMax2;
            curMax2 = curMax1;
        }
        
        return arr;
    }
}
