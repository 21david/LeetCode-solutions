# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i

# TC: O(N)
# SC: O(1)
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = []
        cons = 1  # consecutive streak

        for i in range(len(nums) - 1):
            cons = cons + 1 if nums[i] + 1 == nums[i] else 1

            if i >= k - 1:  # Skip first k - 1 numbers
                ans.append(nums[i] if cons >= k else -1)

        return ans
