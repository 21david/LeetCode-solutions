class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        # start by calculating swaps to place <a on left side of array
        # then create a subset of the remaining elements to calculate swaps to move >b to the right
        # TC = O(N)
        # Aux SC = O(N)

        # Calculate swaps to get <a elements to the left side
        placed_left = 0
        swaps = 0

        for i, n in enumerate(nums):
            if n < a:
                swaps += (i - placed_left)
                placed_left += 1


        # Create subset of remaining elements
        nums2 = [n for n in nums if n >= a]
        N = len(nums2)

        # Calculate swaps to get >b elements to the right side
        placed_right = 0 
        for i in range(N-1, -1, -1):
            n = nums2[i]
            if n > b:
                swaps += ((N-1) - i - placed_right)
                placed_right += 1
                
        mod = 10 ** 9 + 7
        return swaps % mod
