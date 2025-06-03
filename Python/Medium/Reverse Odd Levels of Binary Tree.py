# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
An even better solution would be to implement a custom doubly linked list. 
Whenever we're reversing a level, we can just put a pointer on the front and 
the back of the doubly linked list, reverse, and move the pointers inward 
until they meet in the middle. This would be one pass to reverse with no 
extra space, instead of two passes with O(n) extra space like in the solution 
below.

TC: O(N)
SC: O(N)
'''
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(q):
            # Swap values
            temp_q = deque()
            while q:
                front, back = q.popleft(), q.pop()
                front.val, back.val = back.val, front.val
                temp_q.append(front)
                temp_q.append(back)

            # Put back into original q in the same order, but with swapped values
            while temp_q:
                back = temp_q.pop()
                front = temp_q.pop()
                q.appendleft(front)
                q.append(back)

        # BFS
        q = deque([root])
        odd_level = False

        while q:
            if odd_level:
                # Reverse this level, then add next level
                reverse(q)

            # Optimization to skip the last row
            if q[0].left is None:
                break

            # Add the next level to the queue
            for i in range(len(q)):
                node = q.popleft()
                q.append(node.left)
                q.append(node.right)

            odd_level = not odd_level

        return root

