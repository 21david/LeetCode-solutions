'''
https://leetcode.com/problems/paint-fence
See my other solutions here:
https://github.com/21david/Interview-Kickstart/blob/main/Week%205%20-%20Dynamic%20Programming/Color%20The%20Fence.py
'''

'''
Brute force
TC: (K^N * N)
Auxiliary SC: O(1)
'''
class Solution:
    def numWays(self, n: int, k: int) -> int:
        # See all the possible ways
        # print(list(product(range(k), repeat=n)).__str__().replace(', (','\n('))

        def is_valid_way(way):
            color_streak = 0
            prev_color = None
            for color in way:
                if color == prev_color:
                    color_streak += 1
                    if color_streak == 3:
                        return False
                else:
                    color_streak = 1
                    prev_color = color
            return True

        # Get all possible ways
        ways = product(range(k), repeat=n)

        # Count how many are valid
        return sum(1 for way in ways if is_valid_way(way))
