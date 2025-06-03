class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Build adjacency list
        adj = {}
        for nodes, res in zip(equations, values):
            to, from_ = nodes

            if from_ in adj:
                adj[from_][to] = res
            else:
                adj[from_] = {to: res}
            if to in adj:
                adj[to][from_] = 1 / res
            else:
                adj[to] = {from_: 1 / res}

        # Calculate each query
        ans = []
        for to, from_ in queries:
            if to not in adj or from_ not in adj:
                ans.append(-1.0)
                continue

            # BFS from 'from_' to 'to'
            q = deque([(from_, 1)])
            visited = set()
            found = False
            while q:
                node, prod = q.popleft()
                if node == to:
                    found = True
                    ans.append(prod)
                    break

                for nei, weight in adj[node].items():
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, prod * weight))

            if not found:
                ans.append(-1)

        return ans


'''
Test cases (3 lines per case):
[["a","b"],["b","c"]]
[2.0,3.0]
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]
[["ab","cd"]]
[5.0]
[["a","b"],["c","d"],["a","d"]]
[["a","b"],["b","c"],["ab","cd"]]
[3.0,2.0,5.0]
[["a","b"],["b","c"],["c","d"],["a","d"]]
[["a","b"],["b","c"],["b","d"],["bc","de"]]
[3.0,2.0,1.0,10.0]
[["a","b"],["b","c"],["c","d"],["a","d"],["a","e"],["d","e"],["c","e"],["b","e"]]
[["a","b"],["c","d"]]
[10.0,20.0]
[["a","b"],["c","d"],["aa","bb"],["a","c"]]
[["a","b"],["c","d"],["b","c"]]
[10.0,20.0,2.0]
[["a","b"],["c","d"],["b","c"],["a","d"],["cd","bc"]]


[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]
[["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]]
[2.0,3.0,4.0,5.0,6.0,7.0,8.0]
[["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]]
[["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
[3.0,4.0,5.0,6.0]
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
[ ["a","b"],["b","c"] ]
[2.0,3.0]
[ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
[["a","b"]]
[0.5]
[["a","b"],["b","a"],["a","c"],["x","y"]]
[["a","b"],["b","c"],["bc","cd"]]
[1.5,2.5,5.0]
[["a","c"],["c","b"],["bc","cd"],["ac","cd"]]
[["ab","cd"],["a","c"]]
[4.0,2.0]
[["b","d"]]
[["a","b"],["c","b"],["d","b"],["w","x"],["y","x"],["z","x"],["w","d"]]
[2.0,3.0,4.0,5.0,6.0,7.0,8.0]
[["a","c"],["b","c"],["a","e"],["a","a"],["x","x"],["a","z"]]
[["a","b"],["b","c"],["a","c"]]
[2.0,3.0,6.0]
[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
'''
