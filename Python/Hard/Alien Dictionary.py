class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        # Compare every pair of adjacent words to find a list of edges for our graph
        not_possible = [False]
        def compare_words(word1, word2):
            ans = None
            for i in range(min(len(word1), len(word2))):
                letters.add(word1[i])
                letters.add(word2[i])
                if word1[i] != word2[i]:
                    ans = (word1[i], word2[i]) # (a, b) means 'a comes before b'
                    break
            
            if not ans and len(word1) > len(word2):
                not_possible[0] = True
                return
        
            return ans
        
        letters = set()
        edges = set()

        for i in range(len(words)-1):
            edge = compare_words(words[i], words[i+1])
            if not_possible[0]:
                return ''
            if edge: 
                edges.add(edge)
            for c in words[i]:
                letters.add(c)

        for c in words[-1]:
            letters.add(c)

        # Build an adjacency list
        adj_list = {}
        for u, v in edges:
            if u not in adj_list.keys():
                adj_list[u] = []
            if v not in adj_list.keys():
                adj_list[v] = []
            adj_list[u].append(v)

        # Check for cycles in the graph
        found_cycle = [False]
        def check_cycles_dfs(node, orig_node, count):
            if found_cycle[0]:
                return
            if node == orig_node:
                count += 1
                if count == 2:
                    found_cycle[0] = True
                    return
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    check_cycles_dfs(nei, orig_node, count)

        visited = set()
        for node in adj_list.keys():
            check_cycles_dfs(node, node, 0)
            if found_cycle[0]:
                return ''
            visited = set()

        # Do topological sorting on the graph
        visited = set()
        order = deque()
        def dfs(node):
            for nei in adj_list[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
            order.appendleft(node)

        order = deque()
        
        # Make sure all nodes are visited for the topological sort
        for node in adj_list.keys():
            if node not in visited:
                visited.add(node)
                dfs(node)

        answer = ''.join(order)

        # If there are leftover letters, then there are multiple solutions
        # We can return any solution
        if len(answer) != len(letters):
            return ''.join(list(letters - set(order)) + list(order))

        return ''.join(order)
        
