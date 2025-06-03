# https://leetcode.com/problems/symmetric-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Reverse one of the branches. Then check if it is equal to the other.
Run a DFS or BFS at the same time on both branches to check if they
are equal.

After seeing LeetCode editorial, the DFS/BFS could be modified to solve
the entire problem on its own probably.

TC: O(N)
SC: O(N)
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (root.left and not root.right) or (root.right and not root.left):
            return False
        elif root and not (root.left and root.right):
            return True
        
        # Reverse left branch
        def reverse(node):
            if not node or not (node.left or node.right):
                return
            
            node.left, node.right = node.right, node.left
            reverse(node.left)
            reverse(node.right)
        reverse(root.left)

        # Run DFS on both branches at the same time, checking for equality
        ans = True
        def dfs(node1, node2):
            nonlocal ans
            if not ans:
                return

            # One node exists, the other one doesn't
            elif (node1 and not node2) or (node2 and not node1):
                ans = False
                return

            # Both nodes are None
            elif not (node1 or node2):
                return

            # Therefore, both nodes must exist at this line
            elif node1.val != node2.val:
                ans = False
                return

            dfs(node1.left, node2.left)
            dfs(node1.right, node2.right)
        
        dfs(root.left, root.right)
        return ans
