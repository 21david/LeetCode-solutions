https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """

        # Build adjacency list
        adjList = [[]] * n

        for u, v in edges:
            adjList[u] = adjList[u] + [v]
            adjList[v] = adjList[v] + [u]

        # Do a DFS starting at source. If it finds destination, return true
        # BFS would also work
        stack = [source]
        visited = set()
        while(stack):
            curr = stack.pop()
            if curr == destination:
                return True

            # mark as visited
            visited.add(curr)

            # add neighbors
            for neighbor in adjList[curr]:
                if neighbor not in visited:
                    stack.append(neighbor)

        return False
