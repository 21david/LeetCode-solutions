'''
Binary search for leftmost target and rightmost target. Subtract indices to count number of targets found.
Check if that is greater than the threshold, calculated by len(nums) // 2.

TC = O(logN)
SC = O(1)
'''
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        target_idx_l = bisect_left(nums, target)
        target_idx_r = bisect_right(nums, target)

        num_of_targets = target_idx_r - target_idx_l

        return num_of_targets > (len(nums) // 2)
