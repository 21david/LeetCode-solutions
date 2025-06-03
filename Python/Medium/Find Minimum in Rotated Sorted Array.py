# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        We can solve this with a binary search approach. In every iteration,
        we compare the current number with the number to the left and to the
        right. If we find the point two consecutive numbers are not sorted, 
        then we found the first number of the sorted array and we can
        return it. If the elements are sorted, then we continue the 
        binary search by comparing the current number with the first (or last)
        number of the array.

        Examples:
        [0, 1, 2, 3, 4, 5, 6, 7, 8]

        [2, 3, 4, 5, 6, 7, 8, 0, 1]
         
        [6, 7, 8, 0, 1, 2, 3, 4, 5]
       
        [11,13,15,17]

        [3, 1, 2]

        [4, 5, 1, 2, 3]
        """
      
        l = 0  # low
        h = len(nums)-1  # high
        first = nums[0]
        if first <= nums[h]:  # edge cases: not rotated, or input of size 1
            return first

        # Binary search
        while l <= h:
            m = l + (h - l) // 2  # mid
            if nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m+1] < nums[m]:
                return nums[m+1]
            else:
                if nums[m] > first:
                    l = m + 1
                else:
                    h = m - 1
            
        return -1
