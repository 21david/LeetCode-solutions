'''
Go through each set of consecutive k meetings linearly and calculate what the duration would be
of moving them all to the left as far as possible and to the right as far as possible.

TC: O(N)
SC: O(1)
'''
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        endTime.insert(0, 0)
        startTime.insert(0, 0)
        endTime.append(eventTime)
        startTime.append(eventTime)

        cur_dur = 0

        # calculate total duration of first k meetings
        for i in range(1, k+1):
            cur_dur += endTime[i] - startTime[i]

        # attempt to move to left (or equivalently right) for each set of consecutive k meetings
        ans = 0
        prevI = 0
        nextI = k + 1
        M = len(startTime)
        
        for i in range(1, M-k):
            left_lim = endTime[prevI]
            right_lim = startTime[nextI]
            ans = max(
                ans,
                right_lim - left_lim - cur_dur
            )

            # move to next set
            cur_dur -= endTime[i] - startTime[i]
            cur_dur += endTime[i+k] - startTime[i+k]

            prevI += 1
            nextI += 1

        return ans
©leetcode
