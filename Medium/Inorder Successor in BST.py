# https://leetcode.com/problems/inorder-successor-in-bst/description/
# Basically the same as https://www.tryexponent.com/courses/swe-practice/largest-smaller-bst-key

'''
Solutions 1-3
These perform a DFS on the tree until they find the p node. Then, they keep going
for 1 more node and then store that as the answer, and then stop all other recursive
calls in the stack from exploring more nodes.

Another way to implement this would be to store the previous node in a 'previous'
variable. When that previous variable is equal to p, then store the current node
into the answer variable and return that.
'''
# Solution 1
class Solution(object):
    def inorderSuccessor(self, root, p):

        self.found = False
        self.ans = None

        def dfs(node):
            if node.left:
                dfs(node.left)

            if self.ans:
                return

            if self.found:
                self.ans = node
                return

            if node.val == p.val:
                self.found = True

            if node.right:
                dfs(node.right)

        dfs(root)
        return self.ans

# Solution 2
# This one is the same, but written slightly different
class Solution(object):
    def inorderSuccessor(self, root, p):

        self.found = False
        self.ans = None

        def dfs(node):
            # if not self.ans:
            if node.left:
                dfs(node.left)

            if self.ans:
                return

            if self.found:
                self.ans = node
                return

            if node.val == p.val:
                self.found = True

            if node.right and not self.ans:
                dfs(node.right)

        dfs(root)
        return self.ans

# Solution 3
# This one is also written slightly different. It uses one less variable.
class Solution(object):
    def inorderSuccessor(self, root, p):
        self.ans = None

        def dfs(node):
            if node.left:
                dfs(node.left)

            if self.ans == 'found':
                self.ans = node
                return

            if node.val == p.val:
                self.ans = 'found'

            if node.right and type(self.ans) != TreeNode:
                dfs(node.right)

        dfs(root)
        if type(self.ans) != str:
            return self.ans


'''
Solution 4:
The idea behind this solution is that you are searching for p like a normal BST search.
As you go through nodes, if the current node is greater than p, then we store that into 
a variable. We store only values greater than p because we don't want values lesser than p.
If we haven't found p yet and we found a value lesser than p, we move on to its left subtree
which consists strictly of values less than the current node. So if we store this number,
it will only get updated with numbers lesser than it and greater than p as we traverse the tree.
If we reach the node equal to p, we don't save it, and we continue the traversal to search
the right subtree, which if it exists, will contain the successor. In this case, since we skip
actual p, every node in the right subtree is greater than p, and we will traverse to the
smallest node as a result of searching for p, which will ultimately update our variable to that
smallest value.

This algorithm is a slightly modified version of regular BST. The difference is that if you
find the node you are looking for, since you are looking for its successor, you continue
searching as if p was greater than itself (move on to the right subtree). The result of this is
finding the successor.

It has better time complexity because is runs logarithmically. If the tree is balanced, it
very efficiently rules out half of the nodes at each stage. However, if the tree is skewed,
it can still run in linear time.
'''
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        result = None

        while root:
            if root.val > p.val:  # current node greater than p
                result = root
                root = root.left
            else:  # current node is equal or lesser than p
                root = root.right

        return result



'''
A brute force approach would be to do an in-order DFS traversal and create an
array where all the elements are in order. Then, search for p (binary-search
would optimize this), and then return the next number that is greater than p,
or null if there isn't such a number.

This would have to traverse the entire tree and create an array the size of
the tree, and then another traversal to search for p, so this is the worst
of all the solutions.
'''
