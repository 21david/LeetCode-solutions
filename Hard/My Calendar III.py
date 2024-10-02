'''
https://leetcode.com/problems/my-calendar-iii/

Use a map where the key is a starting or ending time and the value is the
sum of how many meetings start or end at that time. A meeting starting == 1,
and a meeting ending == -1. (If a meeting ends followed by a meeting starting,
it equals to 0, which is kind of like saying there is 1 long meeting if both 
are combined.)

For every booking, add the starting and ending times to the map. Then, kind of like
calculating a prefix sum, go through from start to finish, adding the values. The
value will represent how many meetings are going on at any given time. Return the
maximum that this value reaches.

(Solved after seeing My Calendar II editorial)
'''
from sortedcontainers import SortedDict
class MyCalendarThree:
    def __init__(self):
        self.map: SortedDict = SortedDict()

    def book(self, start_time: int, end_time: int) -> int:
        self.map[start_time] = self.map.get(start_time, 0) + 1
        self.map[end_time] = self.map.get(end_time, 0) - 1
        return max(accumulate(self.map.values()))

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start_time,end_time)
