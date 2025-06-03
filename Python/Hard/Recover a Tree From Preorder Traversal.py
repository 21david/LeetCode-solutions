# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""  
Preorder: P L R

Use a stack:
stack stores nodes and their depth. stack nodes as long as new node has a depth
of 1 more than the previous (if so, it is left child). When it doesn't, pop stack
until it does (in this case it will be the right child).
When we pop a node back from the stack, we can add a child since it will be a node
reference. We build the tree while we do this.

TC: O(N)
SC: O(H), H = height of tree, (which can equal N in the worst case).
"""
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Parse input
        i = j = 0
        nodes_info = []  # stores tuples of (value, depth)

        while j < len(traversal):
            # Traverse dashes
            while traversal[j] == '-':
                j += 1
            depth = j - i

            # Traverse numbers
            i = j
            while j < len(traversal) and traversal[j].isdigit():
                j += 1
            val = int(traversal[i:j])
            nodes_info.append((val, depth))

            i = j

        # Use stack to recover tree
        root = TreeNode(nodes_info[0][0])
        st = [(root, nodes_info[0][1])]  # stores tuples of (node reference, depth)

        for i in range(1, len(nodes_info)):
            node_val, depth = nodes_info[i]
            new_node = TreeNode(node_val)

            if depth == st[-1][-1] + 1:
                # left child 
                prev_node = st[-1][0]
                prev_node.left = new_node
            else:
                # belongs higher up in the tree as a right child
                while st[-1][-1] >= depth:
                    st.pop()

                prev_node = st[-1][0]
                prev_node.right = new_node

            st.append((new_node, depth))

        return root
