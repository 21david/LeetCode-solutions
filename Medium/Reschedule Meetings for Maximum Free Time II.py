# Prefix sum solution
# TC: O(N)
# SC: O(N)
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        M = len(startTime)

        # Build prefix sum going from left to right, which tells us the greatest gap
        # before the left limit of the current meeting (left limit == end of last meeting)
        largestLeft = [0]
        prevGap = startTime[0] - 0
        for i in range(1, M):
            largestLeft.append(max(largestLeft[-1], prevGap))
            prevGap = startTime[i] - endTime[i-1]

        # Now from right to left
        largestRight = [0]
        prevGap = eventTime - endTime[-1]
        for i in range(M - 2, -1, -1):
            largestRight.append(max(largestRight[-1], prevGap))
            prevGap = startTime[i+1] - endTime[i]
        largestRight.reverse()

        # For each meeting, try to move it to far left, or try to move it out
        # if possible. take the max value from those.
        ans = 0
        for i in range(M):
            s = startTime[i]
            e = endTime[i]
            dur = e - s

            # Check moving to the left of current limits
            if i == 0:
                leftLim = 0
            else:
                leftLim = endTime[i-1]

            if i == M-1:
                rightLim = eventTime
            else:
                rightLim = startTime[i+1]

            ans = max(
                ans,
                rightLim - leftLim - dur
            )

            # Check moving out of current limits if possible, using the prefix sums
            currLargestLeft = largestLeft[i]
            currLargestRight = largestRight[i]

            if currLargestLeft >= dur or currLargestRight >= dur:
                ans = max(ans, rightLim - leftLim)

        return ans©leetcode
