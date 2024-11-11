# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0: return 1
        
        wdw = defaultdict(int)
        curr_val = 0

        def add(num):
            nonlocal curr_val
            pos = 0  # bit position
            while num:
                if num & 1:
                    if wdw[pos] == 0:
                        curr_val += 1 << pos
                    wdw[pos] += 1
                pos += 1
                num >>= 1

        def remove(num):
            nonlocal curr_val
            pos = 0  # bit position
            while num:
                if num & 1:
                    if wdw[pos] == 1:
                        curr_val -= 1 << pos
                    wdw[pos] -= 1
                pos += 1
                num >>= 1

        l = r = 0
        ans = math.inf
        while True:
            if curr_val >= k:
                ans = min(ans, r - l)
                remove(nums[l])
                l += 1
            else:
                if r < len(nums):
                    add(nums[r])
                    r += 1
                else:
                    break

        return ans if type(ans) == int else -1


