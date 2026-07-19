# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        ans = 0

        def dfs(n):
            nonlocal ans

            if n is None:
                return 1

            l = dfs(n.left)
            r = dfs(n.right)

            if n.val >= max(l, r):
                ans += 1

            return max(l, r, n.val)

        dfs(root)
        return ans
