"""
https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii

For both trees, paritytition each node into even or odd.
For the second tree:
- Determine whether there are more even or odd nodes.
- Use the larger count.

For the first tree:
- For each node, check if it’s even or odd.
- If it’s even, add the number of even nodes in the first tree 
  to the maximum count (even or odd) from the second tree.
- If it’s odd, do the same.

The problem boils down to counting even and odd nodes in each tree.
Each element in the output is the sum of these counts, but you onlayer
need the maximum count from the second tree, not the minimum.

solved after reading text part of this solution:
https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/solutions/6098836/o-n-m/
"""

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        odd1 = odd2 = even1 = even2 = 0
        N, M = len(edges1) + 1, len(edges2) + 1

        # create adjacency lists
        adj_list1 = [[] for _ in range(N)]
        for a, b in edges1:
            adj_list1[a].append(b)
            adj_list1[b].append(a)

        adj_list2 = [[] for _ in range(M)]
        for a, b in edges2:
            adj_list2[a].append(b)
            adj_list2[b].append(a)

        parity = [0] * N  # get parity group for each node in the first tree

        # bfs first tree
        q = deque([0])
        visited = {0}
        layer = 0
        while q:
            if layer % 2 == 0:
                even1 += len(q)
            else:
                odd1 += len(q)
            for i in range(len(q)):  # do one layer
                node = q.popleft()
                parity[node] = layer % 2
                for nei in adj_list1[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            layer += 1

        # bfs second tree
        q = deque([0])
        visited = {0}
        layer = 0
        while q:
            if layer % 2 == 0:
                even2 += len(q)
            else:
                odd2 += len(q)
            for i in range(len(q)):  # do one layer
                node = q.popleft()
                for nei in adj_list2[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            layer += 1

        max_parity = max(even2, odd2)

        return [(odd1 if parity[i] else even1) + max_parity for i in range(N)]
