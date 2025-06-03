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


'''
Another solution that takes a similar approach but uses
two pointers. This solution is less optimal because it 
uses two pointers.
'''
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
        '''
        We can do a binary search using both p and q values
        at the same time. We will initiate two pointers at the
        root, one for each of the p and q values. They will
        move down the tree depending on the value, just like 
        a regular search through a BST.
        
        We will be at the LCA node when one of these two happen:
        1) Both pointers move to a node that has a value of p
        or q. This means that the other node is somewhere below,
        and the current node is an ancestor, which makes it the
        LCA.
        2) One pointer goes left and the other one goes right
        (p < current node < q) or (q < current node < p)

        So for example, if the two pointers split up after
        the root, then the root is guaranteed to be the LCA.
        '''
        _p = _q = root

        while _p == _q:
            # In the case where one is an ancestor of the other
            # we will return when we find one of them
            if _p == p:
                return p
            elif _q == q:
                return q
            
            curr_node = _p

            # Move pointers using BST logic
            if _p.val > p.val:
                _p = _p.left
            else:
                _p = _p.right

            if _q.val > q.val:
                _q = _q.left
            else:
                _q = _q.right

            if _p != _q:
                # This means that they split up
                return curr_node

        return None
        
