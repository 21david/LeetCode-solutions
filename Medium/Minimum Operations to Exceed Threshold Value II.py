class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappop as pop, heappush as push

        heapify(nums)
        ct = 0

        while nums[0] < k:
            x, y = pop(nums), pop(nums)
            push(nums, min(x, y) * 2 + max(x, y))
            ct += 1
        
        return ct
