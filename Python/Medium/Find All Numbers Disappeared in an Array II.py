class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        nums.sort()

        ans = []
        last = lower
        for i in range(len(nums)):
            curr = nums[i]

            if curr > last:
                ans.append([last, min(curr - 1, upper)])
                last = curr + 1
                if last > upper:
                    break
            elif curr == last:
                last = curr + 1
                if last > upper:
                    break

        if last <= upper:
            ans.append([last, upper])

        return ans
