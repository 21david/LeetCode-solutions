# TC = O(N)
# SC = O(N)
class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        P = len(parent)
        depths = [0] * P

        height = 1
        
        # Adj list to get children of each node, O(N)
        root = 0
        adj = [[] for _ in range(P)]
        for i in range(1, P):
            par = parent[i]
            adj[par].append(i)

        # BFS to figure out depth for each node in O(N)
        q = deque([(0, 1)])
        while q:
            curr, dp = q.popleft()

            depths[curr] = dp
            height = max(height, dp)

            for nei in adj[curr]:
                q.append([nei, dp + 1])

        # Calculare total weighted sum
        ans = 0
        for i in range(P):
            ans += nums[i] * (height - depths[i] + 1)

        return ans

        # Glossed over an AI response to help me figure out the approach
