'''
See my solution article:
https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/solutions/6172672/sorting-greedy-one-pass-beats-100-python-c-java-javascript/

TC: O(NlogN)
SC: O(N) for sorting in Pytnon
'''
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))

        nums.sort()

        # Greedily change numbers in nums to their lowest possible value
        distinct_nums = 0
        target_num = nums[0] - k
        for i in range(len(nums)):
            # If it falls within the range, set nums[i] to it and increment it by 1
            if (nums[i] - k) <= target_num <= (nums[i] + k):
                nums[i] = target_num
                target_num += 1
                distinct_nums += 1

            # If it falls below the range, first update it to the lowest number in the range 
            elif target_num <= nums[i] - k:
                target_num = nums[i] - k
                nums[i] = target_num
                target_num += 1
                distinct_nums += 1

        return distinct_nums
