# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
A way to solve this problem is to do a pre-order traversal while keeping track of
the previously visited node. When you visit a node, rewire the previous node to point
to the current node, and then repeat for the whole tree.

TC: O(N). We must visit every node and rewire it once.
SC: O(H), where H is the height of the tree. In the best case, 
  H == log N (for a balanced binary tree). In the worst case,
  H == N (for a tree with only one node per level, aka each
  node only has one child except the last node).
'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def preorder(node):
            if not node:
                return

            # Save backup for right because it may change
            # before the DFS can use it
            right_backup = node.right

            # Rewire previous node
            if self.prev:
                self.prev.right = node
                self.prev.left = None
            self.prev = node

            # Move on to the next node in pre-order traversal
            preorder(node.left)
            preorder(right_backup)

        preorder(root)
        
