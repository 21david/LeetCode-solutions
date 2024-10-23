# https://leetcode.com/problems/maximum-swap
# TC: O(N)
# SC: O(1)
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10: return num

        num = list(str(num))

        # Store the last index of each digit
        last = [None] * 10
        for i, d in enumerate(num):
            d = ord(d) - 48
            last[d] = i

        # Find the best swap, if any
        for i, d in enumerate(num):
            d = ord(d) - 48

            # Check for the largest number larger than d and that comes after d, if any
            for j in range(9, d, -1):
                if last[j] and last[j] > i:
                    # If we found a greater number, swap
                    num[i], num[last[j]] = num[last[j]], num[i]
                    return int(''.join(num))
        
        # if no swaps could be made (in the case of a non-increasing set of digits I think)
        # just return the number
        return int(''.join(num))
