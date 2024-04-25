# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Base case
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None

        left_half = nums[0 : len(nums) // 2]
        right_half = nums[len(nums) // 2 + 1 : ]

        left_tree = self.sortedArrayToBST(left_half)
        right_tree = self.sortedArrayToBST(right_half)

        root = TreeNode(nums[len(nums) // 2])
        root.left = left_tree
        root.right = right_tree

        return root
      
