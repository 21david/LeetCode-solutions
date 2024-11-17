# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k

# After seeing editorial (except the algorithm or code)
# TC: O(N)
# SC: O(N)
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] + list(accumulate(nums))  # Optimization: reuse nums?
        N, P = len(nums), len(prefix_sum)
        queue = deque([0])
        shortest = math.inf

        for i in range(1, P):
            # Maintain monotonicity in the queue as we add indices
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()
            queue.append(i)

            # Check for any possible valid subarrays, update if found a shorter one
            while prefix_sum[queue[-1]] - prefix_sum[queue[0]] >= k:
                shortest = min(shortest, queue[-1] - queue[0])
                queue.popleft()

        return shortest if shortest <= N else -1
