class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        '''
        In a tree, the number of edges will always be 1 less than
        the number of nodes, and all nodes will form 1 connected
        component. So we can start by checking if the number of edges
        is 1 less than the number of nodes. If so, then we just need
        to make sure that the graph is one connected component and
        optionally that there are no cycles. If we look out for cycles,
        we can optimize the algorithm to stop as soon as it finds a cycle.

        The time complexity is O(N + M). Setting up the empty adjacency list
        is O(N). Filling in the adjacency list is O(M). This is O(N + M) so far.
        The DFS visits each node at most once, and looks through each of it's
        neighbors, so this is also O(N + M). 

        The auxiliary space complexity is O(N + M) also, because the adjacency list
        creates n lists and fills it in with all m edges. (Each edge being added
        twice, once for each node in the edge.) The 'visited' set takes up O(N)
        space. The recursion stack can reach a height of N in the worst case, also
        taking up O(N) space.
        '''

        if len(edges) != n - 1:
            return False

        # Build adjacency list for DFS
        self.adj_list = [[] for _ in range(n)]
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

        # DFS
        self.found_cycle = False
        self.visited = set()
        self.dfs(0, None)

        # If we visited every node, then the graph is one connected
        # compoment, and is therefore a tree
        return len(self.visited) == n
    
    # DFS that looks out for cycles
    def dfs(self, node, prev):
        if self.found_cycle:
            # Don't continue the DFS if a cycle is already found
            return
        
        self.visited.add(node)

        for nei in self.adj_list[node]:
            # If visiting a node that is not the previous node,
            # it should be a new, non-visited node, otherwise there is a cycle
            if nei != prev and nei in self.visited:
                self.found_cycle = True
                return
            elif nei not in self.visited:
                self.dfs(nei, node)
