"""  
TC: O(E)
SC: O(E)
E = number of edges
The number of nodes is bounded by the number of edges in this case,
so the number of nodes doesnt impact the complexities.
"""
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        N = len(amount)

        # Make adjacency list
        table = [None] * N
        for a, b in edges:
            if not table[a]:
                table[a] = Node(a, amount[a])

            if not table[b]:
                table[b] = Node(b, amount[b])

            table[a].add_child(table[b])
            table[b].add_child(table[a])

        # BFS to figure out parent for each node
        q = deque([(table[0], None)])
        visited = set()
        while q:
            node, parent = q.popleft()
            node.parent = parent

            visited.add(node)

            for child in node.children:
                if child not in visited:
                    q.append((child, node))

        # Fast and slow pointer to find mid-way point between Alice and Bob
        bob_n = table[bob]
        fast_ptr = bob_n
        they_meet = True  # Stays true for odd number of nodes path, false for even
        while fast_ptr.parent:
            bob_n = bob_n.parent
            fast_ptr = fast_ptr.parent
            if fast_ptr.parent:
                fast_ptr = fast_ptr.parent
            else:
                they_meet = False

        # Every node from Bob's original node to just before bob_n above becomes 0
        # representing that Bob already opened those gates by the time Alice would get there
        orig = table[bob]
        while orig != bob_n:
            orig.gate = 0
            orig = orig.parent

        # If they meet, they meet at bob_n (half way point)
        if they_meet:
            bob_n.gate //= 2

        # DFS to caculate max path to a leaf node, summing all values along the path
        visited = set()

        def dfs(node):
            if not node.children:
                return node.gate

            visited.add(node.val)

            max_sum = -math.inf
            had_children = False
            for child in node.children:
                if child.val not in visited:
                    max_sum = max(max_sum, dfs(child))
                    had_children = True

            return node.gate + (max_sum if had_children else 0)

        return dfs(table[0])  # DFS starting from the root


class Node:
    def __init__(self, val, gate):
        self.val = val
        self.gate = gate
        self.children = []
        self.parent = None

    def add_child(self, child_node):
        self.children.append(child_node)



"""  
        # BFS to see the tree
        q = deque([table[0]])
        visited = set()
        while q:
            for i in range(len(q)):
                node = q.popleft()
                visited.add(node.val)
                print((node.val, node.gate, [child.val for child in node.children]), end=' ')

                for child in node.children:
                    if child.val not in visited:
                        q.append(child)
            print()
"""
