"""
The observation:
In example 2, taking that whole subarray and summing gives 13, and 13 % 3 == 1,
and each number in the subarray gets a remainder of 1 when divided by 3 as well.
So removing any number in that subarray results in a number divisible by 3, so it
is a "resilient subarray". Because if you subtract a number with remainder 1, then
the whole sum gets that remainder 1 taken away and becomes divisible by 3, as seen
in example 2.

The remainder can be anything from 0 up to k-1, so the solution is to look out for
consecutive numbers with the same remainder, keep their running sum, and when the 
remainder of the sum equals the remainder of all numbers tracked, it forms a 
resilient subarray, track the longest one of those. Reset the group tracking when
a new number has a different remainder.

TC = O(N)
SC = O(N)
"""
class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        N = len(nums)
        prefix_sums = list(accumulate(nums))
        prefix_sums.insert(0, 0)

        prev_remainder = -1  # remainder when divided by k
        consecutive = -1  # number of consecutive number with equal remainders
        ans = 1  # smallest possible answer since subarray length 1 is resilient
        
        for i in range(N):
            curr_remainder = nums[i] % k

            # Extend current group or reset
            if curr_remainder == prev_remainder:
                consecutive += 1
            else:
                prev_remainder = curr_remainder
                consecutive = 1

            # Perfix sum to quickly get the current group's total sum
            curr_sum = prefix_sums[i + 1] - prefix_sums[i - consecutive + 1]

            # If remainder of total sum equals current groups remainder, its a resilient subarray
            if curr_sum % k == prev_remainder:
                ans = max(ans, consecutive)

        return ans
