# TC: O(N)
# Auxiliary SC: O(1)
# Two passes over boxes
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left_ones = 0  # Number of 1s to our left
        left_moves = 0  # Number of moves to move balls on the left

        right_ones = 0  # Number of 1s to our right
        right_index_sum = 0 # Sum of indices of all 1s to our right
        for i, num in enumerate(boxes):
            if num == '1':
                right_ones += 1
                right_index_sum += i

        ans = []
        for i, num in enumerate(boxes):
            # As we move right, each 1 that we have passed will contribute one move
            left_moves += left_ones

            # Find moves required for right 1s with the index_sum, current index, and number of right 1s
            right_moves = right_index_sum - i * right_ones

            ans.append(left_moves + right_moves)

            if num == '1':
                # Move a 1 to the left, update right_index_sum
                right_ones -= 1
                left_ones += 1
                right_index_sum -= i
                
        return ans



'''
Simpler approach after seeing the editorial:
Do a left to right pass to calculate the number of moves to move each ball to each 
position to its right.
Then a right to left pass to calculate the number of moves to move each ball to
each position to its left.
Each pass can be done with two variables. One tracks the number of 1s we've passed,
the other is used to calculate the number of moves to move all those 1s, which is
calculated by adding the value of the first variable to it in each iteration.

TC: O(N)
Auxiliary SC: O(1)
'''
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        answer = [0] * N

        # Left to right pass
        passed_ones = 0
        moves_required = 0
        for i in range(N):
            moves_required += passed_ones
            answer[i] += moves_required
            passed_ones += boxes[i] == '1'

        # Right to left pass
        passed_ones = 0
        moves_required = 0
        for i in range(N - 1, -1, -1):
            moves_required += passed_ones
            answer[i] += moves_required
            passed_ones += boxes[i] == '1'

        return answer
