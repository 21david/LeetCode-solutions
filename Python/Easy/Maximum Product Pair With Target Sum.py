class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        ans = -math.inf
        min_idx_i = min_idx_j = -1
        
        for i in range(N):
            for j in range(N):
                if (nums[i] + nums[j]) == target and nums[i] > nums[j] and nums[i] * nums[j] > ans:
                    ans = nums[i] * nums[j]
                    min_idx_i, min_idx_j = i, j

        return [min_idx_i, min_idx_j]
