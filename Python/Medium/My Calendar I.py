"""
https://leetcode.com/problems/my-calendar-i/description/?envType=daily-question&envId=2024-09-26

One solution would be to keep a sorted array of intervals. Each inner array would have a 
start and end time and be sorted by the start time. Every time we try to book a new meeting, 
we binary search the array and get the intervals that are greater and lesser than the current 
meeting (the two closest intervals after the binary search). Then we would compare the times 
to see if the new interval can be booked. If it can be booked, it would have to be inserted 
into the array (O(N) operation since all the ones to the right would have to be shifted). 
This would result in an O(N^2) solution due to all the shifting. 
Space complexity is equivalent to input size.

A better way would be to use a binary search tree. Each node contains the start and end time. 
When adding a new node (checking if a meeting can be booked), it would do the standard BST 
traversal, except that the two numbers being compared cannot overlap. If they overlap, 
then the meeting can't be booked. If the current meeting never overlaps with any other 
meeting (node), then we just add it to the tree and "book the meeting". This should result 
in an overall O(N log N) approach (still O(N^2) in the worst case for a skewed BST). 
Implementing a self-balancing BST may be an optimization.
Space complexity is equivalent to input size.
"""

# BST Node
class Node:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:
    def __init__(self):
        self.BST = None

    def book(self, start: int, end: int) -> bool:
        # First meeting will always be true
        if self.BST is None:
            self.BST = Node(start, end)
            return True

        prev = None
        true_if_right = False  # Keeps track if temp is right or left child of prev
        temp = self.BST
        while temp:
            prev = temp
            if start >= temp.end:
                temp = temp.right
                true_if_right = True
            elif end <= temp.start:
                temp = temp.left
                true_if_right = False
            else:
                # Either start or end is in the middle of some meeting
                return False

        # If it didnt return false, it can be booked and it needs to
        # be added to the BST
        if true_if_right:
            prev.right = Node(start, end)
        else:
            prev.left = Node(start, end)

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
