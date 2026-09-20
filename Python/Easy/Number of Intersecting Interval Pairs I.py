class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        ans = 0

        for i in range(len(intervals) - 1):
            for j in range(i+1, len(intervals)):
                if intervals[i][1] >= intervals[j][0]:
                    ans += 1

        return ans
