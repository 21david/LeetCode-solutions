# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return helper(root)

def helper(root):
    ans = []

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        ans.append(root.val)
        inorder(root.right)

    inorder(root)
    return ans

        
