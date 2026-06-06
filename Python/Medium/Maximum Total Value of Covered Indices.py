class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        # sliding window
        # we will look for windows in this format: 01 or 0111, or 011111, a zero followed by any number of 1s
        # for each window, calculate total and keep track of min. the min will be where the 0 will optimally be
        # so we subtract the min from the total to get the optimal value for this window and add to final answer
        # this approach works because we can also think of it as moving 0s to the right. A 0 can only move until
        # the next 0 it encounters to its right, so we can basically group substrings like 0111 011 01 01111
        # then for each group we optimize by putting the 0 at the lowest value (minval) which gives the max total.

        n = len(nums)
        l = 0
        ans = 0
        
        while l < n:
            if s[l] == '0':
                total = minval = nums[l]
                r = l + 1
                
                # expand window
                while r < n and s[r] == '1':
                    total += nums[r]
                    minval = min(minval, nums[r])
                    r += 1
                    
                ans += total - minval  # this represents 'moving' that 0 to the lowest number in that group
                l = r
            else:
                # these are initial 1s that can't be moved, just add their number to the final answer
                ans += nums[l]
                l += 1

        return ans
            
