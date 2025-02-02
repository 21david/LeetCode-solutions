'''
After seeing this solution:
https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/solutions/6360032/diagonals/

The furthest point will lie in one of the quadrants. 
With a brute force / greedy approach, we can try to push it as far as we can in each of
the quadrants, and check which one gives us the farthest distance.
For example, we try the NE quadrant. We count every move that is either N or E as 1,
and for S and W moves, we use up a k on it to make it N or E until we run out. When
we run out, then we just follow the path as normal, always recording if we found a
new maximum distance.

We start over for each quadrant then return the longest distance found at any point.

TC: O(S)
SC: O(1)
'''
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        tests = [
            {'N', 'E'},
            {'S', 'E'},
            {'S', 'W'},
            {'N', 'W'}
        ]
        k_copy = k
        furthest_distance = 0

        for good_directions in tests:
            # using these two 'good' directions, we will greedily change 'bad' directions
            # into one of these directions for as many times as we can (k), so that our
            # current sitance goes up rather than down
            current_distance = 0
            k = k_copy
            for current_move in s:
                if current_move in good_directions:
                    current_distance += 1
                else:
                    # try to change if possible
                    if k > 0:
                        current_distance += 1
                        k -= 1
                    else:
                        current_distance -= 1
                
                # record if we found a new furthest distance
                furthest_distance = max(furthest_distance, current_distance)

        return furthest_distance
