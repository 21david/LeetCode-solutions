class Solution {
    public int sumOfGoodIntegers(int n, int k) {
        int ans = 0;
        
        for (int x = Math.max(0, n - k); x <= n + k; x++) {
            if ((x & n) == 0)
                ans += x;
        }

        return ans;
    }
}
