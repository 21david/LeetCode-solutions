"""  
Sliding window. Greedily flip 0s to 1s when possible. When 'k' 0s have been
flipped, for every new 0, remove the oldest 0 and add the new 0. The deque
helps to do this quickly. Always check if the current window length is a new
max.

TC: O(N)
SC: O(K)

This can be improved to SC O(1) by removing the queue, and when we need to
remove the oldest 0, we can repeatedly remove from the left side until we
encounter the 0. However, this would perform more instructions overall 
because we would need to scan linearly instead of jumping to the index of
the oldest 0.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        flipped = deque()
        l = r = 0
        max_len = 0

        while r < N:
            curr_digit = nums[r]

            if curr_digit == 0:
                if k > 0:
                    if len(flipped) == k:
                        # Remove oldest 0 and add newest 0
                        oldest_idx = flipped.popleft()
                        l = oldest_idx + 1
                        flipped.append(r)
                    
                    else:
                        flipped.append(r)
                else:
                    l = r + 1

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len
            
