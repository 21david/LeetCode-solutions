# https://leetcode.com/problems/univalued-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # None or leaf nodes
        if not root or not (root.left or root.right):
            return True

        left = self.isUnivalTree(root.left)
        right = self.isUnivalTree(root.right)
        
        return left and right and ((not root.left) or root.left.val == root.val) and ((not root.right) or root.right.val == root.val)
        
