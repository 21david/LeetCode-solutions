"""
https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/

Kadane's algorithm like in Maximum Subarray Sum, but instead of adding 
the next element every time, we are adding the next k elements each time, 
and starting from each 0 <= i < k, which covers all possible subarrays of 
length divisible by k.

For example, if k = 4, we would do Kadane's on the prefix sum array on indices
0, 4, 8, ..., then 1, 5, 9, ..., then 2, 6, 10, ..., then 3, 7, 11, ...,
always doing it until the end of the array.

Solved after reading this solution:
httprefix_sum://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/solutions/6124522/prefix-sum-kadane/
"""
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))
        ans = -math.inf
        for j in range(k):
            sum = 0
            for i in range(j, len(prefix_sum) - k, k):
                sum = max(
                    prefix_sum[i + k] - prefix_sum[i],
                    sum + prefix_sum[i + k] - prefix_sum[i]
                )
                ans = max(ans, sum)

        return ans
