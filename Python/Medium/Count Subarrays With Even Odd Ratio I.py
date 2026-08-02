# TC = O(N^2)
# SC = O(1)
class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        # Brute force with sliding window
        ans = 0
        rat = a / b
        N = len(nums)
        
        for i in range(N):
            odd = even = 0
            for j in range(i, N):
                odd += nums[j] & 1
                even += (nums[j] & 1 ) == 0

                if odd and even / odd <= rat:
                    ans += 1

        return ans
