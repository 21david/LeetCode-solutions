# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14
# The question boils down to longest contiguous streak of the max number in the array
# Since performing AND can only make two numbers either stay the same value or decrease, and a subarray of 1 counts

# One-pass solution
# TC: O(N)
# SC: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_streak = 1
        max_val = 0
        streak = 0

        for num in nums:
            if num > max_val:
                streak = 1
                max_val = num
                max_streak = 1
            elif num == max_val:
                streak += 1
            else:
                max_streak = max(max_streak, streak)
                streak = 0
        
        return max(max_streak, streak)


# Another one-pass solution
# TC: O(N)
# SC: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        max_streak = 1
        max_val = 0
        streak = 0
        i = 0

        while i < N:
            if nums[i] >= max_val:
                # If we found a new max, any previous streaks are incorrect
                if nums[i] > max_val:
                    max_val = nums[i]
                    max_streak = 1

                # If its equal to the previous max, we need to check if there is a longer streak
                # Traverse any repetitions of the current number
                streak = 1
                i += 1
                while i < N and nums[i] == max_val:
                    streak += 1
                    i += 1

                # Check if the streak was a new max
                max_streak = max(max_streak, streak)
            else:
                i += 1

        return max_streak
