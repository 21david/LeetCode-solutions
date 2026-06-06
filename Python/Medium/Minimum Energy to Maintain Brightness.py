# TC: O(nlogn)
# SC: O(n)
# n = len(intervals)
class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        # Merge intervals (O(n log n))
        # for each interval, take difference, then calculate bulbs required, multiply by time units
        # and return the total (O(n))

        intervals.sort()

        new = []
        inprog = intervals[0]  # interval in progress
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if inprog[0] <= curr[0] <= inprog[1]:
                # if the next one overlaps currenly in progress one, merge it
                inprog[1] = max(inprog[1], curr[1])
            else:
                # now this group of intervals has been fully merged, start on the next one
                new.append(inprog)
                inprog = intervals[i]

        # add the last group since the for loop doesn't add it
        new.append(inprog)


        # for each interval, calculate needed energy. No overlaps since intervals have been merged.
        ans = 0
        for s, e in new:
            units = e - s + 1
            ans += ceil(brightness/3) * units

        return ans
