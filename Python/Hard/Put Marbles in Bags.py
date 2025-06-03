from heapq import heappop as pop, heapify
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        min_heap = [weights[i] + weights[i+1] for i in range(len(weights)-1)]
        max_heap = [-(weights[i] + weights[i+1]) for i in range(len(weights)-1)]
        heapify(min_heap)
        heapify(max_heap)

        max_res = min_res = 0
        for _ in range(k-1):
            max_res += -pop(max_heap)
            min_res += pop(min_heap)

        return max_res - min_res

"""
The final equation will only contain:
    weights[0] 
    weights[-1]
    k-1 pairs of weights[i] and weights[i+1]
In other words, the first and last numbers, and k-1 pairs of
adjacent numbers (can include the first and last nums again).

When we subtract the maximized equation with the minimzed equation,
the first and last numbers cancel since they will be present in both,
so we can just worry about the pairs inside.

The max answer will just be the largest k-1 pairs, and same
for the min. We can just either use a heap to get the k-1 largest
and smallest, or sort. The final answer is just the difference.

I think sort does O(nlogn) one time but sorts the whole array,
where heap does nlogn operation twice as much, but only as much
as necessary (k-1 times). Most optimal depends on inputs I think.

Heap version:
TC: O(K log N)
SC: O(N)
Where N = len(weights)


Example 1:
weights = [1,3,5,1], k = 2

Sorted possible pairs of ends and starts:
(3+5=8)
(5+1=6)
(1+3=4)

8 - 4 = 4
"""
