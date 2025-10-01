class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # Turn into adjacency list (0-based indices)
        adj = [[] for _ in range(n)]
        for u, v, w in connections:
            adj[u-1].append((v-1, w))
            adj[v-1].append((u-1,w))

        mst = prim(adj, 0)

        if len(mst) != n - 1:
            # Graph is not one connected component
            return -1
        return sum(weight for u, v, weight in mst)


# Prim's Algorithm to find the Minimum Spanning Tree (MST) (from notes)
def prim(graph, start):
    # List to store the edges of the MST
    mst = []  
    # Set to track visited vertices
    visited = set()  
    # Min-heap to select the edge with the smallest weight
    min_heap = []  
    # Initialize the heap with edges from the starting node
    def add_edges(node):
        # Mark the node as visited
        visited.add(node)
        
        # Add all edges from the node to the heap
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, node, neighbor))
    
    # Start the algorithm from the initial node
    add_edges(start)

    while min_heap:
        # Get the edge with the minimum weight
        weight, u, v = heapq.heappop(min_heap)  

        # If the node v is not visited, add the edge to the MST
        if v not in visited:
            mst.append((u, v, weight))  # Add the edge to the MST
            
            # Add all edges from the new node v to the heap
            add_edges(v)  
    
    # Return the constructed Minimum Spanning Tree (MST)
    return mst
