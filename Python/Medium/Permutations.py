# https://leetcode.com/problems/permutations

# 19 ms, beats 76.24%
# 13.44 MB, beats 55.76%

# Time complexity: O(N!)

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.perms = []
        self.permutations(nums, [])
        return self.perms

    def permutations(self, nums, temp):
        if nums == []:
            self.perms += [temp]

        for i in range(len(nums)):
            num = nums[i]
            new_nums = nums[:i] + nums[i+1:]
            self.permutations(new_nums, temp + [num])
