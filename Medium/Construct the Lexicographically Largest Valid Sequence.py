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
