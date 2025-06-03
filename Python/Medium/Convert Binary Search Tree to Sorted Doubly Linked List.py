"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        '''
        A way to solve this problem is to do an in-order traversal while keeping
        track of the previous node. For each node that is visited after first
        visiting the smallest value node in the tree, we use the pointer to the
        previous node to rewire that node and the current node. After doing this 
        for all nodes in the tree, we also need to rewire the first and last nodes
        so that they connect to each other.

        Rough pseudocode:
        loop until all nodes traversed:
            recurse left
            if leaf-node and no prev yet, set prev and return
                also save the first node to connect it with last node later
            rewire
            set prev
            recurse right

        prev should be the last node, so connect it with the first node

        TC is O(N) because every node is visited one time.
        SC is O(H) because 'node' will take up memory for every call in
            the call stack. When the algorithm reaches the deepest leaf
            node, there will be H calls in the stack, each storing a 
            pointer to its node.
            In the best case, H is log N (making SC O(logN)) if the tree
            is balanced. 
            In the worst case, H is N (making SC O(N)) if the tree is skewed.
        '''
        if not root:
            return None

        self.first = None
        self.prev = None

        def inorder(node):
            # If first not found yet and we've gone as far left as possible
            if not self.first and not node.left:
                # then this is the lowest node in the BST
                self.first = self.prev = node

            if node.left:
                inorder(node.left)

            # Rewire nodes
            # 'self.prev' prevents rewiring before reaching the smallest node
            # 'and self.prev != node' prevents the first node rewiring to itself
            if self.prev and self.prev != node:
                self.prev.right = node
                node.left = self.prev
                self.prev = node

            if node.right:
                inorder(node.right)
        
        inorder(root)

        # Connect first and last nodes
        self.first.left = self.prev
        self.prev.right = self.first

        return self.first


'''
Another solution. Same approach but written
with less conditionals.
'''

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        '''
        TC is O(N) because every node is visited one time.
        SC is O(H) because 'node' will take up memory for every call in
            the call stack. When the algorithm reaches the deepest leaf
            node, there will be H calls in the stack, each storing a 
            pointer to its node.
            In the best case, H is log N (making SC O(logN)) if the tree
            is balanced. 
            In the worst case, H is N (making SC O(N)) if the tree is skewed.
        '''
        if not root:
            return None

        self.first = None
        self.prev = None

        def inorder(node):
            if node.left:
                inorder(node.left)

            if self.prev:
                self.prev.right = node
                node.left = self.prev
            else:
                self.first = node
                
            self.prev = node

            if node.right:
                inorder(node.right)
        
        inorder(root)

        # Connect first and last nodes
        self.first.left = self.prev
        self.prev.right = self.first

        return self.first



'''
Another way to solve this with similar time and space complexities would
be to use an approach where you travel from node to node with a pointer.
This would require adding a 'parent' attribute to each node, so that we
can travel from a node to anywhere else in the tree. If this is done 
(which can be done as we are traversing the tree for the first time), 
then we can use BST logic to travel from a node to its successor node.
We would first navigate to the lowest value node in the tree, set a 'prev'
pointer to it, and repeatedly travel to the successor node and rewire
them every time, and then just rewire the first and last nodes at the end.
There are rules that can get us to a node's successor node every time,
and every node would still be visited only one time if done this way.
This would be an iterative approach with O(N) TC (because every node will 
be visited once and every edge traveled on once or twice), and O(N) SC 
because we would need a reference to the parent for each node. We
would also need to delete the parent reference at the end if the problem
requires that.
'''
