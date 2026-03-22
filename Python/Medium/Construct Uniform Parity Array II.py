# TC = O(NlogN) for sorting, otherwise O(N)
# SC = O(N) for sorting in Python, otherwise O(1)
class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        nums.sort()

        e = o = 0  # 'evenable', 'oddable', meaning can be made even or can be made odd
        even_count = odd_count = 0 

        for num in nums:
            if num & 1:
                o += 1
                if odd_count:
                    # if at least 1 odd that is smaller, this can be made even
                    e += 1

                odd_count += 1
                    
            else:
                e += 1
                if odd_count:
                    # if at least 1 odd that is smaller, this can be made odd
                    o += 1

                even_count += 1

        # if either even_count or odd_count reached length of nums, that means every number
        # can either be made odd or even or both
        if len(nums) in (e, o):
            return True
        return False©leetcode
