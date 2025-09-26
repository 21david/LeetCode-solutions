class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        ans = 0
        for i in range(N - 1):
            if nums[i] == 0:
                # These cannot form a triangle at all
                continue
            for j in range(i + 1, N):
                # Binary search for last number that forms triangle
                target_len = nums[i] + nums[j]
                last = bisect.bisect_left(nums, target_len)
                ans += last - j - 1
        
        return max(0, ans)

# TC = O(N^2 log N)
# SC = O(N) for Python sorting
