# https://leetcode.com/problems/monotonic-array

# 761 ms, beats 64.05%
# 23.82 MB, beats 68.83%
 
class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Time complexity is O(N) since we traverse the list only once (i goes from 0 to len(nums) without restarting).
        Space complexity is O(1) since we only ever use 'i', 'difference', and 'increasing'.
        """

        if len(nums) <= 2:
            return True

        i = 1
        while i < len(nums) and nums[i] == nums[0]:
            i += 1

        if i == len(nums):
            return True

        increasing = True if nums[i] - nums[0] > 0 else False

        i += 1
        while i < len(nums):
            difference = nums[i] - nums[i-1]
            i += 1
            if difference == 0:
                continue
            elif difference < 0 and increasing:
                return False
            elif difference > 0 and not increasing:
                return False

        return True
