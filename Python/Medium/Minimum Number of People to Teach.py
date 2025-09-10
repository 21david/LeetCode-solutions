"""  
Brute force:
Put the known languages of each person in a set, perhaps store in an array of sets or map of sets
For each language (max 500 iterations), do a DFS or BFS through the entire graph:
    Create a set to represent users that need to learn this language
    For each edge, if one of the nodes doesn't know the language, add the language to the created set
    After the entire traversal, the length of this set is the number of people that would need to learn this language
    Check if it is a new minimum
Once all languages are checked, return the min variable which represents the least number of people to teach

TC = O(N * len(F)), full graph traversal (F) for every language (N)
SC = O(len(L))
    Temporary set for each language iteration, O(len(L)) max
"""
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert to sets for efficient lookup
        languages = [set([lang - 1 for lang in person]) for person in languages]

        ans = math.inf

        # Consider each languages as the taught language
        # check how many would need to be taught for each one
        for lang in range(n):
            to_teach = set()

            # Traverse all edges to find num of people that would need this language
            for u, v in friendships:

                # If two friends can already communicate, no need to learn the language
                if len(languages[u-1] & languages[v-1]):
                    continue

                # Does u know the language?
                if lang not in languages[u-1]:
                    to_teach.add(u)

                # Does v know the language?
                if lang not in languages[v-1]:
                    to_teach.add(v)

            ans = min(ans, len(to_teach))

        return ans
