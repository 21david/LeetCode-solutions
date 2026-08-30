class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cts = Counter(nums)
        ans = 0
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j] == nums[i]:
                    j += 1
                else:
                    break
                    
            if j - i == cts[nums[i]]:
                # special
                ans += 1

            i += 1
            
        return ans
            
