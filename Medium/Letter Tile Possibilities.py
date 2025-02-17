"""
Permutations algorithm, which gets all permutations of all lengths of the string, 
puts each one in a set, then returns the length of the set. 

TC: O(N!)
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()

        def permutations(slate, tiles):
            if tiles == '':
                sequences.add(''.join(slate))
                return
            if slate:
                sequences.add(''.join(slate))

            for i in range(len(tiles)):
                slate.append(tiles[i])
                permutations(slate, tiles[:i] + tiles[i+1:])
                slate.pop()

        permutations([], tiles)
        return len(sequences)
