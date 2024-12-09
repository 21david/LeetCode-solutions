'''
https://leetcode.com/problems/two-best-non-overlapping-events

Gist of this solution:
For each interval, we use binary search to find the maximum value after its end, and we
keep track of the maximum value we find (either single value, or pair of two values),
leading to an O(NlogN) solution.

The binary search is done on a list of [index, max_val] pairs. For example,
[5, 10] means that starting at index 5, the maximum value for any interval starting on 
or after 5 is 10. So for any interval ending at 4, we can add 10 and check if that is a new max.

To create the array of these pairs, we sort the intervals by start, traverse backwards,
and for each start index, we store the greatest value we've seen. Then we convert this
map into a sorted array to do binary search. A BST might also work.

TC: O(NlogN) - Sorting, then N binary searches 
SC: O(N) - for sorting and for max_after dictionary/array
'''
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[0])  # Sort by start

        # Build map of indices and maximum value at or after that index        
        E = len(events)
        max_after = {}
        max_val = 0
        for i in range(E-1, -1, -1):
            ev_start, ev_end, val = events[i]
            max_val = max(max_val, val)
            max_after[ev_start] = max(max_after.get(ev_start, 0), max_val)

        # Convert to array for binary searching
        max_after = [[k, v] for k, v in max_after.items()]
        M = len(max_after)

        # For each event, binary search on max_after to find largest value after its end
        # Check if each pair is a new max
        ans = 0
        for ev_start, ev_end, val in events:
            # If its either before or after all indices, we won't find an interval
            if ev_end < max_after[-1][0] or ev_end >= max_after[0][0]:
                ans = max(ans, val)
                continue

            # Start binary search
            l = 0
            r = M - 1
            while l <= r:
                mid = l + (r - l) // 2

                if max_after[mid][0] > ev_end:
                    l = mid + 1
                else:
                    r = mid - 1
            
            ans = max(ans, val + max_after[r][1])

        # Return greatest value we found
        return ans

'''
Test cases:
[[1,3,2],[4,5,2],[2,4,3]]
[[1,3,2],[4,5,2],[1,5,5]]
[[1,5,3],[1,5,1],[6,6,5]]
[[1,5,5],[2,6,3],[3,7,4],[8,10,6],[8,11,3],[11,13,4],[2,12,10]]
[[1,3,2],[1000000000,1000000000,10]]
[[2,1000000000,1000000],[1,1,1000000]]
'''
