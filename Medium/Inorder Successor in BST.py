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


