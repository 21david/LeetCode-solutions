'''
BINARY SEARCH:
Sort by start points.
Make an array of just the start points (optional, could use sorted intervals)
Go through each interval from start to end
For each endpoint, binary search for the start point that is closest to it on its left side, or equal
The index of this one minus the current index gives the total intervals this interval overlaps with
Repeat for all for final answer
O(NlogN) because N for each iteration, logN for each binary search
'''
class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        N = len(intervals)
        intervals.sort(key = lambda x: x[0])
        starts = [interval[0] for interval in intervals]
        starts.append(math.inf)
        ans = 0

        from bisect import bisect_right
        
        for i in range(N):
            st, end = intervals[i]
            idx = bisect_right(starts, end)
            
            if starts[idx] != end:
                idx -= 1
                
            ans += idx - i

        return ans
