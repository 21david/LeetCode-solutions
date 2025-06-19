// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/?envType=daily-question&envId=2025-06-19

class Solution {
    public int partitionArray(int[] nums, int k) {
        Arrays.sort(nums);

        // In a loop, greedily pick first one, then greedily pick all that are <= k different
        int ans = 0;
        int curr = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - curr <= k)
                continue;
            else {
                curr = nums[i];
                ans++;
            }
        }

        // Add 1 for the last group
        return ans + 1;
    }
}
