# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return find_depth(root, 0)

def find_depth(tree, depth):
    if tree == None:
        return depth
    return max(find_depth(tree.left, depth+1), find_depth(tree.right, depth+1))
