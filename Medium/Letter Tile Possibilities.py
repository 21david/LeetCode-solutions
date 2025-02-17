# See my solution post on this problem:
# https://leetcode.com/problems/letter-tile-possibilities/solutions/6431955/on-table-lookup-precomputed-results-beat-hhws

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



# Precomputed results for each frequency of letters
# TC: O(N), N = number of letters in tiles
# SC: O(L), L = number of unique letters in tiles
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        frequencies = Counter(tiles).values()
        frequencies_of_frequencies = Counter(frequencies)

        match len(tiles):
            case 1:
                match frequencies_of_frequencies:
                    case {1: 1}:
                        return 1
            case 2:
                match frequencies_of_frequencies:
                    case {2: 1}:
                        return 2
                    case {1: 2}:
                        return 4
            case 3:
                match frequencies_of_frequencies:
                    case {3: 1}:
                        return 3
                    case {2: 1, 1: 1}:
                        return 8
                    case {1: 3}:
                        return 15
            case 4:
                match frequencies_of_frequencies:
                    case {4: 1}:
                        return 4
                    case {3: 1, 1: 1}:
                        return 13
                    case {2: 2}:
                        return 18
                    case {1: 2, 2: 1}:
                        return 34
                    case {1: 4}:
                        return 64
            case 5:
                match frequencies_of_frequencies:
                    case {5: 1}:
                        return 5
                    case {4: 1, 1: 1}:
                        return 19
                    case {3: 1, 2: 1}:
                        return 33
                    case {1: 2, 3: 1}:
                        return 63
                    case {2: 2, 1: 1}:
                        return 89
                    case {1: 3, 2: 1}:
                        return 170
                    case {1: 5}:
                        return 325
            case 6:
                match frequencies_of_frequencies:
                    case {6: 1}:
                        return 6
                    case {5: 1, 1: 1}:
                        return 26
                    case {4: 1, 2: 1}:
                        return 54
                    case {1: 2, 4: 1}:
                        return 104
                    case {3: 2}:
                        return 68
                    case {3: 1, 2: 1, 1: 1}:
                        return 188
                    case {1: 3, 3: 1}:
                        return 363
                    case {2: 3}:
                        return 270
                    case {2: 2, 1: 2}:
                        return 522
                    case {1: 4, 2: 1}:
                        return 1010
                    case {1: 6}:
                        return 1956
            case 7:
                match frequencies_of_frequencies:
                    case {7: 1}:
                        return 7
                    case {6: 1, 1: 1}:
                        return 34
                    case {5: 1, 2: 1}:
                        return 82
                    case {1: 2, 5: 1}:
                        return 159
                    case {4: 1, 3: 1}:
                        return 124
                    case {4: 1, 2: 1, 1: 1}:
                        return 349
                    case {1: 3, 4: 1}:
                        return 679
                    case {3: 2, 1: 1}:
                        return 447
                    case {2: 2, 3: 1}:
                        return 649
                    case {1: 2, 3: 1, 2: 1}:
                        return 1265
                    case {1: 4, 3: 1}:
                        return 2467
                    case {2: 3, 1: 1}:
                        return 1840
                    case {1: 3, 2: 2}:
                        return 3591
                    case {1: 5, 2: 1}:
                        return 7012
                    case {1: 7}:
                        return 13699
