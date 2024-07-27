# https://leetcode.com/problems/minimum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """
        Do a BFS. When the first leaf node is found, it will
        be at the minimum depth, because the BFS travels from
        the top level to the bottom, one by one.

        N = number of nodes in the tree
        Time complexity: O(N)
            Best case scenario: The minimum depth is 2, no matter how big the tree is.
            For inputs like this, the time complexity would be O(1).
            Worst case scenario: Full binary tree (forms an isosceles triangle). For
            inputs like this, the BFS would have to traverse half the nodes (all levels
            except the last one). The time complexity for these inputs is O(N).
        Space complexity: O(N)
            Best case scenario: binary tree where each node only has one child.
            In this case, the queue will only ever have 1 node at the most, making
            the time complexity O(1).
            Worst case scenario: Full binary tree (forms an isosceles triangle).
            After the BFS finishes the second last level, all nodes in the last level
            will be in the queue, which is half the nodes in the entire tree. If N is
            increased, this will increase linearly with it. The space complexity for
            these type of inputs would be O(N).
        """
        if not root:
            return 0

        # BFS
        # Use a deque because it offers O(1) time complexity
        # for adding and removing on both the start and the end
        q = deque()
        q.append((root, 1))
        while q:
            curr_node, level = q.popleft()
            if not (curr_node.left or curr_node.right):  # leaf node
                return level
            
            # Add children to queue
            if curr_node.left:
                q.append((curr_node.left, level+1))

            if curr_node.right:
                q.append((curr_node.right, level+1))

        return 0
        
