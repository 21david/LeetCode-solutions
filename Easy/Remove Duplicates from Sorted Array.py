# https://leetcode.com/problems/remove-duplicates-from-sorted-array

# 49 ms, beats 96.32%
# 14.68 MB, beats 48.72%

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        One pointer (i) will traverse the whole array looking for duplicates.
        Another pointer (k) will gradually set the numbers in the beginning
        as i traverses the array and finds new unique numbers.

        O(N) time complexity
        O(1) space complexity
        '''

        i, k = 0, 0

        nums_len = len(nums)

        while i < nums_len:
            # 'i' will traverse all duplicates of current number
            while i+1 < nums_len and nums[i+1] == nums[i]:
                i += 1

            # at this point, 'i' has traversed all duplicates of the
            # current number

            # officially set the value at index 'k' and move on to
            # the next index and number
            nums[k] = nums[i]
            k += 1
            i += 1

        return k
