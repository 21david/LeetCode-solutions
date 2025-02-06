'''
Heap and sorting approach:
Sort in descending order by nums1 one, then gradually pick the first k elements along 
with the corresponding elements in nums2. The goal is to repeatedly remove the index 
that has the lowest element in nums2 because that's the one that holds it back, and 
then replace it with the next best one, which would be the next greatest element that 
hasn't been taken from the sorted nums1. If multiple elements have the same value in 
nums2, then we have to pick the one with the lowest value in nums1 because that 
contributes the least to the score. This should be done until there are no more 
elements that we can pick, at which point we return the greatest score that we found. 
This should be an O(n log n) time complexity approach.

TC: O(NlogN)
SC: O(N) - for the sorted indices array O(N) and the heap O(K)
'''
from heapq import heapify, heappop as pop, heappush as push
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)

        # Sort nums1 descending. O(NlogN)
        nums1_idxs_sorted = list(range(N))
        nums1_idxs_sorted.sort(key = lambda i: -nums1[i])

        # Add largest k elements (using nums1 values) to the heap. O(K)
        heap = []
        for i in range(k):
            new_idx = nums1_idxs_sorted[i]
            heap.append((nums2[new_idx], nums1[new_idx], new_idx))
        heapify(heap)

        # Calculate current score. O(K)
        sum_val = sum(nums1_val for nums2_val, nums1_val, idx in heap)
        min_val = min(nums2_val for nums2_val, nums1_val, idx in heap)
        ans = sum_val * min_val

        # For as many times as we can, remove least effective pair from the current k pairs
        # and replace with the next best one. We are using the smallest value of nums2 to 
        # remove the least effective pair to try to get a higher score. For ties with the value
        # of nums2, we use the smallest value of nums1. O(NlogN)
        for new_idx in nums1_idxs_sorted[k:]:
            # Remove lowest pair from the current set
            old_nums2_val, old_nums1_val, old_idx = pop(heap)

            # Get a new pair using the next index in nums1_idxs_sorted and push it to the heap
            new_nums1_val = nums1[new_idx]
            new_nums2_val = nums2[new_idx]
            push(heap, (new_nums2_val, new_nums1_val, new_idx))

            # Update the values used to calculate the score
            sum_val -= old_nums1_val
            sum_val += new_nums1_val

            # If the minimum went up with the new pair, update it
            if old_nums2_val < heap[0][0]:
                min_val = heap[0][0]

            # Check if new score is a new record
            ans = max(ans, sum_val * min_val)

        return ans

'''
Test case
[4, 6, 1, 9, 10, 20, 30]
[2, 9, 9, 2, 1, 2, 3]
4

=> 130

Explanation:
[6, 9, 20, 30] => 65  (sum)
[9, 2, 2, 3] => 2  (min)
65 * 2 = 130
'''
