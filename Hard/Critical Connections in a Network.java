//  https://leetcode.com/problems/critical-connections-in-a-network/

// 103 ms, faster than 63.67%
// 103.5mb, less than 73.01%
// Solved in 50 minutes using solution at  youtube.com/watch?v=erlX-1MJlv8&t=2s
class Solution {
    ArrayList<ArrayList<Integer>> adjList = new ArrayList<>();
    List<List<Integer>> solution = new ArrayList<List<Integer>>();
    
    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        // convert to an adjacency list
        for(int i = 0; i < n; i++) {
            adjList.add(new ArrayList<Integer>());  // initialize a list for each node
        }
        int a, b;
        for(List<Integer> connection : connections) {
            // for each connection [a, b], add b to a's list in the adjList, and vice versa
            a = connection.get(0);
            b = connection.get(1);
            adjList.get(a).add(b);
            adjList.get(b).add(a);
        }
        
        visited = new boolean[n];
        visitedTimes = new int[n];
        lowTimes = new int[n];
        
        // do a dfs
        dfs(0, -1);  // 0 as the current node, -1 as the parent (no parent)
        
        return solution;
    }
    
    boolean[] visited;
    int[] visitedTimes;
    int[] lowTimes;
    int time = 0;
    
    public void dfs(int currNode, int parentNode) {
        visited[currNode] = true;
        visitedTimes[currNode] = lowTimes[currNode] = time++;

        // iterate through neighbors
        for(int neighbor : adjList.get(currNode)) {
            if(neighbor == parentNode)  // skip if already visited
                continue;

            if(!visited[neighbor]) {
                dfs(neighbor, currNode);
                lowTimes[currNode] = Math.min(lowTimes[currNode], lowTimes[neighbor]);
                
                if(visitedTimes[currNode] < lowTimes[neighbor])
                    solution.add(Arrays.asList(currNode, neighbor));
            }
            else {
                lowTimes[currNode] = Math.min(lowTimes[currNode], visitedTimes[neighbor]);
            }
        }
        
    }
}

/*
Sample input:
4
[[0,1],[1,2],[2,0],[1,3]]
10
[[0,1],[0,2],[1,3],[2,3],[3,4],[2,5],[5,6],[5,7],[5,8],[6,7],[7,8],[6,9],[7,9],[8,9]]
*/
