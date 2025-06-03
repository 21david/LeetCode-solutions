# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
BFS approach, processing one layer at a time to find its maximum value.
TC: O(N)
SC: O(N)
'''
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root: 
            return answer

        q = deque([root])
        while q:
            # Find max value in the current row
            max_val = -math.inf
            for i in range(len(q)):
                node = q.popleft()
                max_val = max(max_val, node.val)

                # Add next row to the queue to process later
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

            answer.append(max_val)

        return answer
