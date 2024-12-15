"""
https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions

General approach:
Step 1: For the second day, perform a BFS or a DFS on each currency
to find out the conversion rate from that currency to the initial currency.
Store the final results for each currency in a map.

Step 2: For the day 1 graph, start a BFS on the initial currency.
For each node you reach, multiply the current conversion rate by the conversion
rate calculated in Step 1. This will be one possible rate.
Do this for all nodes in day one and record the maximum conversion rate.
Return the maximum conversion rate at the end.

Note: If you can't reach the initial currency on day two, the answer is 1,
because no profits can be made in this case.

I rushed this during the competition, so there's a lot of space for improvement,
such as optimizing the set operations and related logic.
"""
class Solution:
    def maxAmount(
        self, 
        init: str, 
        pairs1: List[List[str]], 
        rates1: List[float], 
        pairs2: List[List[str]], 
        rates2: List[float]
    ) -> float:

        # Build adjacency list for day one
        n1 = len(pairs1)
        adj1 = {}
        for i in range(n1):
            curr_from, curr_to = pairs1[i]
            rate = rates1[i]
            if curr_from not in adj1:
                adj1[curr_from] = []
            adj1[curr_from].append((curr_to, rate))

            if curr_to not in adj1:
                adj1[curr_to] = []
            adj1[curr_to].append((curr_from, 1 / rate))

        # Build adjacency list for day two
        n2 = len(pairs2)
        adj2 = {}
        for i in range(n2):
            curr_from, curr_to = pairs2[i]
            rate = rates2[i]
            if curr_from not in adj2:
                adj2[curr_from] = []
            adj2[curr_from].append((curr_to, rate))

            if curr_to not in adj2:
                adj2[curr_to] = []
            adj2[curr_to].append((curr_from, 1 / rate))

        # BFS to find conversion rate to initial currency in day two
        def bfs_to_init(node):
            visited = set()
            queue = deque([(node, 1)])  # Queue stores (currency, conversion_rate)
            while queue:
                curr, curr_rate = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr == init:
                    return curr_rate
                for next_curr, next_rate in adj2[curr]:
                    queue.append((next_curr, curr_rate * next_rate))

        # Check if initial currency exists in day two
        currencies_in_day2 = set()
        for curr_from, curr_to in pairs2:
            currencies_in_day2.add(curr_from)
            currencies_in_day2.add(curr_to)
        if init not in currencies_in_day2:
            return 1.0

        # Precompute conversion rates from day two to initial currency
        rates2_map = {}
        for node in adj2:
            rate_to_init = bfs_to_init(node)
            rates2_map[node] = rate_to_init

        max_rate = 0
      
        # BFS in day one to compute maximum conversion rate
        visited = set()
        queue = deque([(init, 1)])  # Queue stores (currency, conversion_rate)
        while queue:
            curr, curr_rate = queue.popleft()
            # Compute possible rate and update max conversion rate
            max_rate = max(max_rate, curr_rate * (rates2_map.get(curr, -math.inf) or 1))
            if curr not in adj1:
                continue
            for next_curr, next_rate in adj1[curr]:
                if next_curr not in visited:
                    visited.add(next_curr)
                    queue.append((next_curr, curr_rate * next_rate))

        return max_rate

'''
Good test case:
"AAA"
[["AAA","BBB"],["AAA","CCC"],["AAA","DDD"],["BBB","FFF"],["CCC","EEE"],["EEE","GGG"]]
[2.0, 4.0, 6.0, 3.0, 1.0, 2.0]
[["BBB","AAA"],["FFF","AAA"],["GGG","AAA"],["AAA","DDD"]]
[2.0, 4.0, 5.0, 2.0]
'''
