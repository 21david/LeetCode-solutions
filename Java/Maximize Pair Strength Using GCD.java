// TC = O(N^2 * log(max(nums))). GCD algorithm is O(log(min(a,b))), and we're doing it on all N^2 pairs of integers.
// SC = O(log(max(nums)). GCD algorithm uses stack space in the order of log(max(nums)). All other variables 0-dimensional.
class Solution {
    public long maxPairStrength(int[] nums) {
        double ans = 0;

        for (int i = 0; i < nums.length - 1; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                double str =  ((long) nums[i] * nums[j]) / Math.pow(gcd(nums[i], nums[j]), 2);
                ans = Math.max(ans, str);
            }
        }

        return (long) ans;
    }

    public static int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }
}
