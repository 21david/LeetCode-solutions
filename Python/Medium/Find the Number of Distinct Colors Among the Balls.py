"""
Make one dictionary/array that stores the current color of a ball.
Make another dictionary/array that stores the frequency count of each color.
When a frequency goes down to 0, delete it, so that the size of the 
dictionary always gives the number of distinct colors.
Iterate through queries, keep the dicts/arrays updated, and use the size of the 
second one as the answers of the output array.

Note: Arrays cause MLE due to 10^9 constraint on limit and color.

TC: O(Q)
SC: O(Q) (using dictionaries. O(L) using arrays.)
"""
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        answer = []
        ball_color = defaultdict(int)
        color_frequency = defaultdict(int)

        for ball, color in queries:
            # Check if ball already had a color
            old_color = ball_color[ball]
            if old_color >= 1:
                color_frequency[old_color] -= 1
                if color_frequency[old_color] == 0:
                    del color_frequency[old_color]

            # Update dictionaries and calculate a new answer
            color_frequency[color] += 1
            ball_color[ball] = color
            answer.append(len(color_frequency))

        return answer
