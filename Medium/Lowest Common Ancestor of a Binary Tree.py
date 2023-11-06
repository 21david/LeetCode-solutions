# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
# 43 ms, beats 73.24%
# 25.6 MB, beats 40.17%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        found_node = root.val == p.val or root.val == q.val

        if found_node:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if (left and right) or (found_node and (left or right)):
            return root
        elif left or right:
            return left or right

