class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        # Sorting based solution
        def find_max_val(num):
            return (int(''.join(sorted(str(num), reverse=True))))
            
        rearranged = [find_max_val(num) for num in nums]

        # Sort all nums by how much they would gain from a rearrangement, highest first
        nums_with_gains = [(rearranged[i] - nums[i], nums[i]) for i in range(len(nums))]
        nums_with_gains.sort(key = lambda x: -x[0])

        # For the first k numbers, add the gain from their rearrangement
        # then just add the numbers without their gain
        ans = 0
        for gain, num in nums_with_gains:
            if k:
                ans += gain
                k -= 1
            
            ans += num

        return ans
