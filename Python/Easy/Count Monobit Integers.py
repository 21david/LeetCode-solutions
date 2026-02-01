class Solution:
    def countMonobit(self, n: int) -> int:
        bin_len = len(bin(n)[2:])
        ans = 1

        max_num = 2 ** (bin_len) - 1

        for i in range(bin_len - 1, 0, -1):
            ans += 1

        if n == max_num:
            ans += 1

        return ans©leetcode
