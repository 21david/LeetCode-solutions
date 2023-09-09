class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = []
        k = 0
        i = 0
        while i < len(nums):
            # check for duplicates
            while i+1 < len(nums) and nums[i+1] == nums[k]:
                i += 1
            
            # at this point, i is at the last duplicate number
            uniques += [nums[i]]
            k = i+1
            i += 1

        # copy uniques back onto original list
        i = 0
        for num in uniques:
            nums[i] = num
            i += 1
        
        return len(uniques)
            




        
