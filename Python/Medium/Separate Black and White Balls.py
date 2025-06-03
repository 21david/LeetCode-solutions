"""
https://leetcode.com/problems/separate-black-and-white-balls

So this problem can just be seen as how many swaps it takes to move
either all the zeros into their place or all the ones into their place.
So if you pick the zeros, you could just calculate the distance that each zero
needs to travel to get into its place.

One way to do this would be to have a counter that counts how many zeros have
been found, and then iterate through each index. If we find a zero, then we
subtract the index from the counter to see how many swaps it takes to move
that zero into its place. The counter represents the index that the next zero
should go in.

If you do this for all the balls, you should get the total number of swaps
to get every zero into its final place. This would be a linear algorithm
with O(1) space complexity.
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        count = ans = 0
        for i, ball in enumerate(s):
            if ball == '0':
                ans += i - count
                count += 1
        return ans
