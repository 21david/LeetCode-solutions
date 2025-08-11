# TC = O(R * C), each element will only be visited at most once. Pointers only go towards the right and never back.
# SC = O(R), for the pointers array
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        R = len(mat)
        pointers = [0] * R  # each element is the index (pointer) of the current number for that row

        max_val = max(row[0] for row in mat)

        while True:
            all_equal = True  # Assume all pointers point to an equal value
            for r in range(R):
                # "keep up" the current pointer to the current max_val, or the next one if max_val not in this row
                for j in range(pointers[r], len(mat[r])):
                    if mat[r][j] >= max_val:
                        break
                if mat[r][j] < max_val:
                    # This row doesn't have the max_val, so there is no common element
                    return -1
                
                pointers[r] = j

                # If the last row didn't have max_val, we restart with the new max_val
                if mat[r][j] > max_val:
                    max_val = mat[r][j]
                    all_equal = False
                    break
            
            # If the for loop completed, then all pointers point to an equal value
            if all_equal:
                return mat[0][pointers[0]]  # Arbitrarily pick the first row's pointer element
