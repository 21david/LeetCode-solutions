# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/solutions/6777023/bfs-and-math-o-n-time-and-space-explained-code/
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        
        # build adj list
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adj[u-1].append(v-1)

        # bfs to find max level
        q = deque([0])
        level = 0  
        
        while q:
            # process one level
            for i in range(len(q)):
                nd = q.popleft()

                # add neighbors to queue
                for nei in adj[nd]:
                    q.append(nei)
            level += 1 

        # Increase digit limit since the numbers get big
        sys.set_int_max_str_digits(100000)

        return (2 ** (level - 2)) % mod
