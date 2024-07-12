# leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Sliding window technique. We can track the following things: The index of the last
        0 we found, the index of the first 1 of the current subarray of 1s (the left side of
        the window), the length of the current subarray, and the maximum length we've found.
        To start, we iterate through each number and check if it is a 1 or a 0. If it is a 1
        we just add to the current subarray and update the maximum-length variable if it is
        a new maximum. If it is a 0, then we check if it's the first 0 we've found (good way
        is to check if the index of the first 0 is within the array or if it's still set to
        it's initial value, which we can set to -1 to represent that we haven't found a 0).
        If it is, then we update variable for the index of the first 0 and continue. If it 
        isn't, then we have to move the window to the right (this is done by updating the 
        variable for the index of the first 1 to the right of the last 0, by simply adding 1),
        remove the number of consecutive 1s before that last 0 (this is done by subtracting
        the index of the new 0 from the index of the first one to get the number of 1s that
        we need to subtract, then subtracting that result from the current-length variable),
        and then updaing the index of the last 0 to the current one. This effectively slides
        the window to the right and keeps the length of the current subarray correct.
        At the end, if no 0s were found, we have to subtract 1 from the maximum-length variable,
        otherwise, we just return it.

        Small optimization: We skip any consecutive 0s at the beginning, but then we need
        to make modifications to make sure we are deleting 1 element from the array
        (for example, array of all 1s will need a 1 subtracted, array with trailing 0s
        may need one of those 0s to be the deleted element)

        Variables:
        index_of_last_zero
        index_of_first_one
        current_length
        max_length

        Time complexity: O(N) because we only pass over the array one time.
        Auxiliary space complexity: O(1) because we only use constant extra space.
        """

        # Skip trailing 0s
        index_of_first_one = 0
        while index_of_first_one < len(nums) and nums[index_of_first_one] == 0:
            index_of_first_one += 1

        if index_of_first_one == len(nums):
            # Edge case: There are no 1s
            return 0

        index_of_last_zero = -1
        current_length = 1
        max_length = 1

        for i in range(index_of_first_one + 1, len(nums)):
            if nums[i]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                if index_of_last_zero < 0:
                    index_of_last_zero = i
                else:
                    # If a 0 had already been found, slide window to the right
                    # from the previous 0 to the new 0
                    num_of_old_ones = index_of_last_zero - index_of_first_one
                    current_length -= num_of_old_ones
                    index_of_first_one = index_of_last_zero + 1
                    index_of_last_zero = i

        if index_of_last_zero == -1:
            if nums[0] == 0:
                return max_length
            else:
                return max_length - 1
        else:
            return max_length


    """
    Another solution with the same basic approach, but using different variables
    and logic. Also O(N) space complexity and O(1) time complexity.
    """
    def longestSubarray_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        """

        index_of_last_zero = -1
        index_of_second_last_zero = -1
        current_length = 0
        max_length = 0
        removed_zero = False

        for i in range(0, len(nums)):
            if nums[i]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                if not nums[i-1]:
                    removed_zero = False
                    current_length = 0
                elif not removed_zero and current_length >= 1:
                    removed_zero = True
                elif removed_zero and current_length >= 1:
                    # If a 0 had already been found AND it was counted as a removed 0
                    # slide window to the right to the next 0
                    if index_of_second_last_zero:
                        num_of_old_ones = index_of_last_zero - index_of_second_last_zero - 1
                    else:
                        num_of_old_ones = index_of_last_zero
                    current_length -= num_of_old_ones
                index_of_second_last_zero = index_of_last_zero
                index_of_last_zero = i
                
        if index_of_last_zero == -1:
            return max_length - 1
        else:
            return max_length
