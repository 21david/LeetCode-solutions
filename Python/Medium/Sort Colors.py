# https://leetcode.com/problems/sort-colors

# Dutch National Flag problem
# TC: O(N)
# SC: O(1)
class Solution:
    def sortColors(self, nums):
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        r = -1
        w = 0
        for b in range(len(nums)):
            if nums[b] == 0:
                r += 1
                swap(r, r + w)
                if nums[b] in (2, 0):
                    swap(b, r)
            elif nums[b] == 1:
                w += 1
                swap(r + w, b)


# Same approach as above
# TC: O(N)
# SC: O(1)
# From IK
class Solution:
    def sortColors(self, nums):
        rIdx = 0 # every element behind is a 0 (R)
        wIdx = 0 # every element behind is a 0 (R) or a 1 (W)
        i = 0  # to iterate the array
        
        while i < len(nums):
            if nums[i] == 1:
                nums[i], nums[wIdx] = nums[wIdx], nums[i]
                wIdx += 1
            elif nums[i] == 0:
                nums[i] = nums[wIdx]
                nums[wIdx] = nums[rIdx]
                nums[rIdx] = 0
                rIdx += 1
                wIdx += 1
                
            i += 1


# Counting sort
# TC: O(N)
# SC: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = w = b = 0
        for num in nums:
            match (num):
                case 0:
                    r += 1
                case 1:
                    w += 1
                case 2:
                    b += 1
        
        i = 0
        while r:
            nums[i] = 0
            i += 1
            r -= 1
        while w:
            nums[i] = 1
            i += 1
            w -= 1
        while b:
            nums[i] = 2
            i += 1
            b -= 1
        
