'''
https://leetcode.com/problems/special-array-ii

Each element in nums belongs to some special subarray. We can label 
each element with its group number. We can use the nums array directly,
or we could also create an auxiliary array.
For each query, we just index into the start and end, and check if both 
have the same group number.

TC: O(N + Q)
Aux SC: O(1) - no new data structures created
'''
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Label each special subarray (override nums)
        group = 0
        for i in range(1, len(nums)):
            num_copy = nums[i-1]  # backup before overriding w/ group num
            nums[i-1] = group
            if nums[i] % 2 == num_copy % 2:
                # End of previous interval, start of a new interval
                group += 1

        nums[-1] = group  # Set the last element

        # For each query, check if the start and the end are part of 
        # the same special subarray (override queries)        
        for i in range(len(queries)):
            queries[i] = nums[queries[i][0]] == nums[queries[i][1]]

        return queries
