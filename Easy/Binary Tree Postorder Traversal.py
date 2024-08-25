# https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Recursive solution.
TC: O(N)
SC: O(N)
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode], list=None) -> List[int]:
        if not root:
            return None
        if list is None:
            list = []
        self.postorderTraversal(root.left, list)
        self.postorderTraversal(root.right, list)
        list.append(root.val)
        return list


'''
Recursive one-line solution
TC: O(N)
SC: O(N)
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []


'''
"Follow up: Recursive solution is trivial, could you do it iteratively?"
'''

'''
To do this iteratively, we can use a stack-based DFS. However, to prevent processing a 
node as soon as we reach it (which would result in a regular pre-order traversal), we 
can check if we've already processed all of the left and right child nodes first and 
then print it. If we haven't visited either of the child nodes, we can put it back in 
the stack without printing it. Null nodes can count as 'visited'. This way, it will be 
revisited in the future when both of its children have already been processed.
This approach gives us the correct left-right-parent processing order.

TC: O(N). Every node is processed either once or twice at most.
SC: O(N). The `children_visited` dictionary will store information for each node. The 
stack may store the whole tree if it is completely skewed. Neither of these data 
structures will ever store more than the amount of nodes in the tree. The answer array 
will store one value for every node in the tree.
'''
LEFT = 0
RIGHT = 1
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        stack = [root]
        children_visited = { root: [False,False] }
        answer = []

        while stack:
            current_node = stack.pop()

            # Put in children_visited dict if not already
            if current_node not in children_visited:
                children_visited[current_node] = [False,False]

            current_children_visited = children_visited[current_node]

            # If still some children to visit, put back in stack and visit children first
            if not all(current_children_visited):
                stack.append(current_node)

            # If both children subtrees already processed, we can process the node
            else:
                answer.append(current_node.val)
                continue
            
            # Right, then left, so the result is DFS visits left child before right
            if current_node.right:
                stack.append(current_node.right)
            current_children_visited[RIGHT] = True

            if current_node.left:
                stack.append(current_node.left)
            current_children_visited[LEFT] = True

        return answer


'''
Much simpler solution. Post-order is left-right-parent. The reverse is
parent-right-left, which is a slight variation of pre-order (parent-left-
right). Pre-order is already very easy to implement, even with this 
variation. So if we do it this way, all we have to do is either reverse 
the list at the end, or create the list backwards to begin with. Doing it 
this backwards way with a deque (double-ended queue, using linked lists) 
is better because we avoid the extra O(N) operation of reversing it at the 
end.

TC: O(N)
SC: O(N)
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        stack = [root]
        answer = deque()

        while stack:
            current_node = stack.pop()
            answer.appendleft(current_node.val)

            if current_node.left:
                stack.append(current_node.left)

            if current_node.right:
                stack.append(current_node.right)

        return answer

