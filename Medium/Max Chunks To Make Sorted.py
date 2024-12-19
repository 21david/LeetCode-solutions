"""
Keep track of the max number. While the current 
index is less than the max number, move to 
the next index, always looking out for a new 
max. When the max equals the index, that 
is one chunk. Repeat until the end of the 
array. This ensures that each number will 
reach its final position and starts a new chunk 
whenever it can.

TC: O(N)
SC: O(1)
"""
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num = -1
        chunks = 0
        for i in range(len(arr)):
            max_num = max(max_num, arr[i])
            chunks += max_num == i

        return chunks
