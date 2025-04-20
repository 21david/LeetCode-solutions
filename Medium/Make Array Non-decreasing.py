"""
Sorting + Set:
make an array with the values and their indices
sort this array by descending value and descending index
take the largest value, put all indices to its right into a set of used
    add 1 to answer
keep checking the next largest until we find one that isn't in the set
    add 1 to answer
put every index from this index to previous index into the set
repeat until all numbers are 'used'

TC: O(N log N)
SC: O(N)
"""
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        # Set up the array
        N = len(nums)
        answer = 1
        with_indices = list(zip(nums, range(len(nums))))
        with_indices.sort(key = lambda x: (-x[0], -x[1]))

        # Process the largest element and all indices to the right
        used = set()
        largest, idx = with_indices[0]
        for i in range(idx, N):
            used.add(i)

        # Repeatedly process the next largest element to the left
        prev = idx
        for i in range(1, N):
            largest, idx = with_indices[i]
            if idx in used:
                continue

            # When we found the next largest element to the left 
            # this becomes one of the numbers in the final array. 
            # We then 'use' all indices to the right up to the 
            # previous element we processed
            answer += 1
            for j in range(idx, prev):
                used.add(j)

            prev = idx

        return answer
        

# After seeing a solution post:
# Add 1 to the answer each time a new max is found
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        max_val = ans = 0
        for num in nums:
            if num >= max_val:
                max_val = num
                ans += 1

        return ans
