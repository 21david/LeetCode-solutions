# LeetCode Premium problem
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""  
TC = O(N), visit each node once in BFS order, addnig to the hash dictionary each time
SC = O(N), hash table stores a copy of each value
"""
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)

        # BFS
        q = deque([(root, 0)])
        min_col = max_col = 0
        while q:
            node, col = q.popleft()
            if not node:
                continue
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            # Add to the list for this collumn
            cols[col].append(node.val)

            # Add children
            q.append((node.left, col - 1))
            q.append((node.right, col + 1))

        # Seen in editorial: To avoid sorting, we can iterate between min_col and max_col
        # and get all the lists in order
        return [cols[col] for col in range(min_col, max_col + 1)] if cols else []

