# Sliding window approach
# Window of side k moves from left to right, calculating the new profits with the modifications applied each time
# TC = O(N)
# SC = O(1)
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        max_sum = sum(p * s for p, s in zip(prices, strategy))

        half_k = k // 2

        # Set up window in the first position and calculate its profit
        current_sum = max_sum
        for i in range(half_k):
            if strategy[i] == -1:
                current_sum += prices[i]
            elif strategy[i] == 1:
                current_sum -= prices[i]

        for i in range(half_k, half_k + half_k):
            if strategy[i] == -1:
                current_sum += 2 * prices[i]
            elif strategy[i] == 0:
                current_sum += prices[i]

        max_sum = max(max_sum, current_sum)

        # Move the window to the right until it reaches the end
        N = len(prices)
        for i in range(1, N - k + 1):
            # Restore previous value (that just got out of the window)
            if strategy[i-1] == -1:
                # Turn into a 0
                current_sum -= prices[i-1]
            elif strategy[i-1] == 1:
                # Turn into a 0
                current_sum += prices[i-1]

            # Update the halfpoint of the window that just changed (from 1 to 0)
            current_sum -= prices[i + half_k - 1]

            # Update the value that just entered the window (rightmost)
            if strategy[i + k - 1] == -1:
                # Turn into a 1
                current_sum += 2 * prices[i + k - 1]
            elif strategy[i + k - 1] == 0:
                # Turn into a 1
                current_sum += prices[i + k - 1]

            # Check if current window position gives the most profit
            max_sum = max(max_sum, current_sum)

        return max_sum
