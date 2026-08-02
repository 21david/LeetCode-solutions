class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        ans = 0
        N = len(nums)
        
        for i in range(N-1):
            for j in range(i + 1, N):
                res = (nums[i] * nums[j]) / math.gcd(nums[i], nums[j]) ** 2
                ans = max(ans, res)

        return int(ans)
