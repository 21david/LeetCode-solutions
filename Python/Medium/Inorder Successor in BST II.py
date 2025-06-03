# https://leetcode.com/problems/inorder-successor-in-bst-ii

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

'''
Find the successor:
- If the node has a right subtree, successor is somewhere in that tree (its the smallest element in that tree)
    - Move pointer to right subtree, then go left as much as possible
- If node has no right subtree:
    - If node is a right child, then successor is the first ancestor that is not a right child
        - Move up until you are at a node that is a left child
    - If the node is a left child, successor is the parent
This is all derived from BST logic.
'''

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node.right:
            # Find smallest in right subtree
            node = node.right
            while node.left:
                node = node.left
            return node
        else:
            # Find the first ancestor that is greater than it
            while node.parent and node.parent.val < node.val:
                    node = node.parent
            # If it reaches this point, if it has no parent, then there is no successor
            # Otherwise, this parent is the first ancestor that is greater than it, which
            # equates to the in-order successor.
            # We can imagine it is going diagonally top-left as much as it can, and when it
            # makes a 'right turn' (moves diagonally top-right), it reached the successor node
            if not node.parent:
                return None
            else:
                return node.parent
            
