# https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        if root.left == None and root.right == None:
            if root.val == targetSum:
                return True

        return traverse(root, 0, targetSum, 0)
        

def traverse(root, sum, targetSum, depth):
    if root != None and root.left == None and root.right == None:  # if leaf node
        if sum + root.val == targetSum and depth >= 1:
            return True
        else:
            return False
    elif root == None:
        return False
    
    return traverse(root.left, sum + root.val, targetSum, depth + 1) or traverse(root.right, sum + root.val, targetSum, depth + 1)
