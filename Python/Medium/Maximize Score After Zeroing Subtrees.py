import math
from collections import deque

"""
Time Complexity: O(n)
- Building the adjacency list, generating the level-order list, computing 
  bottom-up subtree sums, and running the final BFS each visit every node 
  and edge a constant number of times.

Space Complexity: O(n)
- The adjacency list, traversal order list, skipset, sums array, and BFS 
  queue each store at most n elements.
  
^ Written by Gemini Argon

Code below written by me, cleaned up by Argon
"""
class Solution:
    def maxScore(self, parent: list[int], op: list[int], score: list[int]) -> int:
        n = len(parent)

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for i, par in enumerate(parent):
            if par != -1:
                adj[par].append(i)

        # Build top-down traversal order starting from the root
        order = [0]
        for node in order:
            order.extend(adj[node])

        """
        Process nodes bottom-up to accumulate subtree sums so parent nodes 
        can evaluate child subtrees in O(1) time. Rather than zeroing out 
        entire subtrees in-place, record the root of each zeroed subtree in 
        skipset and exclude those branches during a final top-down BFS. This
        avoids quadriatic time complexity.
        """
        skipset = set()
        sums = score.copy()

        for i in reversed(order):
            curr_children = adj[i]
            if not curr_children:
                continue  # skip leaf nodes until we get to the parent nodes

            # Process subtree (min element helps decide if we should zero out,
            # sum later helps upper nodes decide which to zero out if at all)
            child_sum = 0
            min_sc = math.inf
            min_sc_i = -1
            for j in curr_children:
                child_sum += sums[j]
                if sums[j] < min_sc:
                    min_sc = sums[j]
                    min_sc_i = j

            # Zero out the minimum child subtree if required (op == 1) 
            # or if doing so increases the score (op == 0 and min_sc < 0)
            if op[i] == 1 or min_sc < 0:
                skipset.add(min_sc_i)
                child_sum -= min_sc

            sums[i] = child_sum + score[i]

        # Final traversal top-down via BFS, summing all nodes outside skipped subtrees
        # Since we made optimal decisions above, this gives the sum of the maximum score
        queue = deque([0])
        total = 0
        
        while queue:
            curr = queue.popleft()
            total += score[curr]
            
            for child in adj[curr]:
                if child not in skipset:
                    queue.append(child)

        return total
