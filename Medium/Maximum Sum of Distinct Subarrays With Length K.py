# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dic = Counter(nums[:k])
        curr_sum = sum(k * v for k, v in dic.items())
        max_seen = 0

        if len(dic) == k:
            max_seen = max(max_seen, curr_sum)

        for i in range(k, len(nums)):
            newest_num = nums[i]
            dic[newest_num] += 1
            curr_sum += newest_num

            oldest_num = nums[i - k]
            dic[oldest_num] -= 1
            curr_sum -= oldest_num
            if dic[oldest_num] == 0:
                del dic[oldest_num]

            if len(dic) == k:
                max_seen = max(max_seen, curr_sum)

        return max_seen
