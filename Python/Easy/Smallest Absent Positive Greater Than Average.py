class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        if abs(avg - ceil(avg)) <= 0.0001:
            avg = ceil(avg)
            avg += 1
        else:
            avg = ceil(avg)
            
        nums = set(nums)
        while avg <= 0 or avg in nums:
            avg += 1
        return avg
