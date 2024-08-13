# https://leetcode.com/problems/count-good-nodes-in-binary-tree

'''
Based on my understanding, a node is good if all it's subtrees have the same size.
So for every node, we need to know the size of each of its subtrees (unless it only has
1 or 0, then it is automatically a good node.) 

So maybe I could build the tree out, and probably with a DFS, i can figure out
the sizes of each subtree at each node.
When we find out the first subtree size, we can store that size in a variable in the node.
We will assume each node is good by setting a true boolean to it also.
Every time we add another count for a subtree, we compare it with that variable. If it's
different, then the node will be marked not good forever. 
At the end, we found how many good nodes remain.

Another approach might be to count how many nodes there are in total while doing the DFS.
Then, count how many nodes get marked not-good, and subtract that from the total to get
our final answer. (Solution below implements it like this.)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.first_size = None
        self.good = True

class Solution(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        # Build adj list
        adj = []

        for a, b in edges:
            # expand adj as needed to put nodes into their index
            if not a < len(adj):
                adj.extend( [] for _ in range(a - len(adj) + 1) )
            if not b < len(adj):
                adj.extend( [] for _ in range(b - len(adj) + 1) )

            adj[a].append(b)
            adj[b].append(a)

        # print(adj)

        # Build a tree with BFS
        root = Node(0)
        q = deque([root])
        visited = set()
        visited.add(0)
        while q:
            node = q.popleft()

            for nei in adj[node.val]:
                if nei in visited:
                    continue
                new_child_node = Node(nei)
                node.children.append(new_child_node)
                q.append(new_child_node)
                visited.add(nei)


        # traverse tree with DFS to find good nodes
        self.bad_nodes = 0

        def dfs(node):
            # Leaf node
            if len(node.children) == 0:
                return 1

            first_size = None
            good_node = True
            sizes = []
            total_size = 0
            for child in node.children:
                size = dfs(child)
                if not first_size:
                    first_size = size
                elif good_node:
                    if size != first_size:
                        good_node = False
                total_size += size

            if not good_node:
                self.bad_nodes += 1

            return total_size + 1

        dfs(root)

        # Calculate good nodes
        return (len(edges) + 1) - self.bad_nodes

        
