# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        min_val = min(p.val, q.val)
        max_val = max(p.val, q.val)
        
        while root:
            if root.val >= min_val and root.val <= max_val:
                return root
            elif root.val < min_val:
                root = root.right
            else:
                root = root.left
        
