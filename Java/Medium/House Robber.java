/*
https://leetcode.com/problems/house-robber
DP memoization solution, using similar strategy as subsets algorithm.
*/

class Solution {
    private static int help(int[] nums, int s, Map<Integer, Integer> memo) {
        // if taken or skipped all, return 0
        if (s >= nums.length) return 0;

        // use DP memoization
        if (memo.containsKey(s)) return memo.get(s);

        // take curr num. add 2 to skip adjacent num
        int op1 = nums[s] + help(nums, s+2, memo);

        // skip curr num
        int op2 = help(nums, s+1, memo);

        int max = Math.max(op1, op2);
        
        memo.put(s, max);  // memoize
        return max;
    }

    public int rob(int[] nums) {
        Map<Integer, Integer> memo = new HashMap<>();
        int max = Solution.help(nums, 0, memo);
        return max;
    }
}
