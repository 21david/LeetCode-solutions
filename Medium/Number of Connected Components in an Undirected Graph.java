//  https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

/*
Convert to adjacency list.
You could make a boolean array that marks each node as visited
when it gets visited, then try to do a DFS at each node.
If the node was not visited, then we add 1 to the count of 
connected components. If it was visited already, then we do
nothing and try the next node.
After trying all the nodes, we should have a count of connected
components.
*/
class Solution {
    public int countComponents(int n, int[][] edges) {
        // make an arraylist with n empty arraylists
        ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
        for(int i = 0; i < n; i++)
            adjList.add(new ArrayList<>());
        
        // fill in with edges
        for(int[] edge : edges) {
            adjList.get(edge[0]).add(edge[1]);
            adjList.get(edge[1]).add(edge[0]);
        }
        
        boolean[] visited = new boolean[n];
        
        // dfs at each node
        for(int node = 0; node < n; node++) {
            dfs(adjList, node, visited);
        }
        
        return count;
    }
    
    int count = 0;
    
    public void dfs(ArrayList<ArrayList<Integer>> adjList, int node, boolean[] visited) {
        if(visited[node])
            return;
        
        // if not visited, then this is a new component
        // add to count, and visit all the nodes in this component
        count++;
        
        Stack<Integer> stack = new Stack<>();
        stack.push(node);
        
        int curNode;
        while(!stack.isEmpty()) {
            curNode = stack.pop();
            
            if(visited[curNode])
                continue;
            
            visited[curNode] = true;
            
            // visit neighbors
            for(int neighbor : adjList.get(curNode)) {
                stack.push(neighbor);
            }
        }
    }
}

/*
Sample input:
5
[[0,1],[1,2],[3,4]]
5
[[0,1],[1,2],[2,3],[3,4]]
10
[]
100
[[0,1],[0,2],[40,41]]
1
[]
2
[[0,1]]
2
[[1,0]]
*/
