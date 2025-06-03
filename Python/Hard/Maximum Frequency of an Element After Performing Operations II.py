# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii
# Solution post:  https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/solutions/6028818/line-sweep-explained-beats-100-time-beats-100-space/

from sortedcontainers import SortedDict
class Solution:
    def maxFrequency(self, nums: List[int], num: int, numOperations: int) -> int:
        # Line sweep algorithm
        up = [n + num for n in nums]  # upper limit for each number
        down = [n - num for n in nums]  # lower limit for each number
        dictionary = SortedDict()

        for d in down:
            dictionary[d] = dictionary.get(d, 0) + 1

        for u in up:
            dictionary[u+0.1] = dictionary.get(u+0.1, 0) - 1

        for n in nums:
            # For the actual numbers, the value represents their frequency
            dictionary[n+0.01] = dictionary.get(n+0.01, 0) + 1

        overlapping_intervals = 0
        answer = 0
        for num, val in dictionary.items():
            if abs(num - floor(num) - 0.01) < 0.01:  # num is an actual number in nums (ends in 0.01)
                possible_nums = overlapping_intervals - val  # Number of nums that can be extended to this num
                
                # Only consider the current frequency of the current number (val)
                # Plus as many extended numbers as numOperations allows
                answer = max(answer, val + min(possible_nums, numOperations))

            else:  # num is an extended version of a number in nums (ends in .0 or .1)
                overlapping_intervals += val  # Part of line sweep, add or subtract current interval
                answer = max(answer, min(overlapping_intervals, numOperations))  # Only consider as many overlapping intervals as numOperations allows

        return answer
