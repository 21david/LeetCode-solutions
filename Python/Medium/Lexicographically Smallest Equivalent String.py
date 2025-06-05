"""  
TC = O(s1 + baseStr)
Aux SC = O(baseStr) - could be O(1) if strings are mutable
Output SC = O(baseStr)
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # Build adjacency list - O(s1)
        adj = [set() for _ in range(26)]
        for i in range(len(s1)):
            # Each pair represents an bidirectional edge, add it to the adjacency list
            adj[ord(s1[i]) - 97].add(s2[i])
            adj[ord(s2[i]) - 97].add(s1[i])

        # Debug: See adj list
        # for n in range(26):
        #     print(chr(n + 97), adj[n] if len(adj[n]) else '')

        # DFS from each letter to find groups (connected components) - O(26) = O(1)
        map_to_lex_smallest = [-2] * 26
        for i in range(26):
            if map_to_lex_smallest[i] != -2:
                continue  # already visited

            # Gather all letters in the current group into curr_group
            curr_group = []
            stack = [i]
            map_to_lex_smallest[i] = -1

            while stack:
                curr_let = stack.pop()
                curr_group.append(curr_let)

                for nei in adj[curr_let]:
                    code = ord(nei) - 97
                    if map_to_lex_smallest[code] != -1:
                        stack.append(code)
                        map_to_lex_smallest[code] = -1  # mark as visited

            if len(curr_group) == 1: 
                continue

            # Sort to find lexicographically smallest, then map all to that one
            curr_group.sort()
            # print(curr_group, [chr(i + 97) for i in curr_group])

            for letter_code in curr_group:
                map_to_lex_smallest[letter_code] = curr_group[0]

        # print(map_to_lex_smallest)

        # Build answer - O(baseStr)
        ans = []
        for letter in baseStr:
            new_letter_idx = map_to_lex_smallest[ord(letter) - 97]

            if new_letter_idx == -1:
                # Letter is not part of a group, don't change it
                ans.append(letter)
            else:
                ans.append(chr(new_letter_idx + 97))

        # Convert to string - O(baseStr)
        return ''.join(ans)
