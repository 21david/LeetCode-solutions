# Backtracking
class Solution:
    def constructDistancedSequence(self, N: int) -> List[int]:
        num_slots = N * 2 - 1
        arr = [-1] * num_slots
        used_set = set()
        answer = None

        # num_used -> how many slots we've set
        # i -> current index
        def backtrack(num_used: int, i: int):
            nonlocal answer
            if answer:
                return  # Lexcographically largest combination already found
            elif num_used >= num_slots:
                # If all slots were successfully set, we've found the answer
                # Since it tries combinations in order from largest to smallest, 
                # the first found answer will be the lexicographically largest
                answer = arr[:]
                return

            if arr[i] != -1:
                backtrack(num_used, i + 1)  # Don't override a number already set

            if answer:
                return  # If above call found answer, don't continue searching

            # For the current slot, try all numbers from largest to smallest
            for n in range(N, 1, -1):
                if n not in used_set and i + n < num_slots and arr[i] == arr[i + n] == -1:
                    # Set the current index and index + n and recurse on the next index
                    arr[i] = arr[i + n] = n
                    used_set.add(n)
                    backtrack(num_used + 2, i + 1)
                  
                    # If the answer was not found, undo the changes and try the next number
                    arr[i] = arr[i + n] = -1
                    used_set.remove(n)

                if answer:
                    return

            # If all larger numbers failed, try 1, but only add one 1
            if 1 not in used_set and arr[i] == -1:
                arr[i] = 1
                used_set.add(1)
                backtrack(num_used + 1, i + 1)
                arr[i] = -1
                used_set.remove(1)

        backtrack(0, 0)
        return answer



"""  
Since there are only 20 possible inputs (1 - 20), we can precompute the
result of each one and store it in a matrix for O(1) retrieval.
The algorithm above was used to precompute these results.
This array has each answer in order, with the index corresponding with n,
so that indexing at n gives the correct answer for n.

TC = SC = O(1)
"""
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # arr[n] = constructDistancedSequence(n)
        return [
            None,
            [1],
            [2, 1, 2],
            [3, 1, 2, 3, 2],
            [4, 2, 3, 2, 4, 3, 1],
            [5, 3, 1, 4, 3, 5, 2, 4, 2],
            [6, 4, 2, 5, 2, 4, 6, 3, 5, 1, 3],
            [7, 5, 3, 6, 4, 3, 5, 7, 4, 6, 2, 1, 2],
            [8, 6, 4, 2, 7, 2, 4, 6, 8, 5, 3, 7, 1, 3, 5],
            [9, 7, 5, 3, 8, 6, 3, 5, 7, 9, 4, 6, 8, 2, 4, 2, 1],
            [10, 8, 6, 9, 3, 1, 7, 3, 6, 8, 10, 5, 9, 7, 4, 2, 5, 2, 4],
            [11, 9, 10, 6, 4, 1, 7, 8, 4, 6, 9, 11, 10, 7, 5, 8, 2, 3, 2, 5, 3],
            [12, 10, 11, 7, 5, 3, 8, 9, 3, 5, 7, 10, 12, 11, 8, 6, 9, 2, 4, 2, 1, 6, 4],
            [13, 11, 12, 8, 6, 4, 9, 10, 1, 4, 6, 8, 11, 13, 12, 9, 7, 10, 3, 5, 2, 3, 2, 7, 5],
            [14, 12, 13, 9, 7, 11, 4, 1, 10, 8, 4, 7, 9, 12, 14, 13, 11, 8, 10, 6, 3, 5, 2, 3, 2, 6, 5],
            [15, 13, 14, 10, 8, 12, 5, 3, 11, 9, 3, 5, 8, 10, 13, 15, 14, 12, 9, 11, 7, 4, 6, 1, 2, 4, 2, 7, 6],
            [16, 14, 15, 11, 9, 13, 6, 4, 12, 10, 1, 4, 6, 9, 11, 14, 16, 15, 13, 10, 12, 8, 5, 7, 2, 3, 2, 5, 3, 8, 7],
            [17, 15, 16, 12, 10, 14, 7, 5, 3, 13, 11, 3, 5, 7, 10, 12, 15, 17, 16, 14, 9, 11, 13, 8, 6, 2, 1, 2, 4, 9, 6, 8, 4],
            [18, 16, 17, 13, 11, 15, 8, 14, 4, 2, 12, 2, 4, 10, 8, 11, 13, 16, 18, 17, 15, 14, 12, 10, 9, 7, 5, 3, 6, 1, 3, 5, 7, 9, 6],
            [19, 17, 18, 14, 12, 16, 9, 15, 6, 3, 13, 1, 3, 11, 6, 9, 12, 14, 17, 19, 18, 16, 15, 13, 11, 10, 8, 4, 5, 7, 2, 4, 2, 5, 8, 10, 7],
            [20, 18, 19, 15, 13, 17, 10, 16, 7, 5, 3, 14, 12, 3, 5, 7, 10, 13, 15, 18, 20, 19, 17, 16, 12, 14, 11, 9, 4, 6, 8, 2, 4, 2, 1, 6, 9, 11, 8]
        ][n]
