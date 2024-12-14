# https://leetcode.com/problems/wiggle-sort
# TC: O(N)
# SC: O(1)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        should_increase = True
        for i in range(len(nums) - 1):
            if (should_increase and nums[i] > nums[i+1]) or (not should_increase and nums[i] < nums[i+1]):
                # Some fixing needs to be done
                nums[i+1], nums[i] = nums[i], nums[i+1]

            should_increase = not should_increase


'''
test case
[9,1,0,5,3,3,6,7,8,4,3,2,10,0,1,2]
'''
