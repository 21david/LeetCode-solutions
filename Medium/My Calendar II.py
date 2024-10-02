'''
Solution using Linked list and Binary search tree.
Use BST to quickly decide if a meeting can be booked.
If it can, add it to the linked list, which is optimized
to merge intervals that touch to improve iteration speed.
Beats 96% in runtime (~175 ms)
'''
class MyCalendarTwo:
    def __init__(self):
        self.BST = None  # Binary Search Tree
        self.LL = None  # Linked List

    def book(self, start: int, end: int) -> bool:
        if not self.LL:
            # If no previous meetings, add and return true
            self.LL = LNode(start, end)
            return True

        # If there aren't any double booked intervals yet, meeting can be booked
        if not self.BST:
            self.add_to_list(start, end)
            return True

        # If there are double intervals, check if any will cause a triple booking - O(logN) search
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
                # Either start or end is in the middle of a double interval
                return False

        # If it didnt return false, it can be booked
        self.add_to_list(start, end)
        return True

    def add_to_list(self, start, end):
        temp = self.LL

        if end < temp.start:
            # It goes at the very beginning
            new_node = LNode(start, end, temp)
            self.LL = new_node
            return
        elif end == temp.start:
            # Goes at very beginning but merges with the first one
            self.LL.start = start
            return

        # ---ITERATE FOR START---
        prev = None
        while temp and start > temp.end:
            prev = temp
            temp = temp.next
        # ---ITERATE FOR START---
        
        if not temp:
            # Goes at the very end
            new_node = LNode(start, end)
            prev.next = new_node
            return
        
        if start < temp.start:
            # There is a gap before temp
            if end < temp.start:
                # It goes in between two nodes
                new_node = LNode(start, end, next=temp)
                prev.next = new_node
                return
            elif end == temp.start:
                # Merge
                temp.start = start
                return
            elif end > temp.start:
                # There is a double interval here
                if end > temp.end:
                    double_interval = [temp.start, temp.end]
                    temp.start = start
                    self.add_to_bst(*double_interval)
                    # don't return, continue searching with 'end' as there may be many more intervals ahead
                elif end == temp.end:
                    double_interval = [temp.start, temp.end]
                    self.add_to_bst(*double_interval)
                    temp.start = start
                    return
                elif end < temp.end:
                    double_interval = [temp.start, end]
                    self.add_to_bst(*double_interval)
                    temp.start = start
                    return

        elif start < temp.end:  # start >= temp.start
            # No gap, current interval start lands on another interval, so definitely a double interval
            if end < temp.end:
                double_interval = [start, end]
                self.add_to_bst(*double_interval)
                return

            else:  # end >= temp.end
                double_interval = [start, temp.end]
                self.add_to_bst(*double_interval)

        elif start == temp.end:
            if not temp.next:
                temp.end = end
                return
            else:
                if end < temp.next.start:
                    temp.end = end
                    return
                elif end == temp.next.start:
                    temp.end = temp.next.end
                    temp.next = temp.next.next
                    return

        # ---ITERATE FOR END---
        while temp and end > temp.end:
            prev = temp
            temp = temp.next

            if temp and end >= temp.end:
                double_interval = [temp.start, temp.end]
                self.add_to_bst(*double_interval)
                # new_interval = [prev.end, temp.start]
                # Merge prev and temp since their gap is now completely covered
                prev.end = temp.end
                prev.next = temp.next
                temp = prev
            elif temp and end <= temp.end:
                # Reached the last interval for this while loop
                if end < temp.start:
                    # No double interval here, just a gap
                    prev.end = end
                    return

                elif end > temp.start:
                    double_interval = [temp.start, end]
                    self.add_to_bst(*double_interval)
                    prev.end = temp.end
                    prev.next = temp.next
                    temp.next = None  # not needed?
                    del temp # temp = prev  # also not needed?
                    return
                
                elif end == temp.start:
                    # No double interval, just a meeting starting right after the meeting being booked
                    prev.end = temp.end
                    prev.next = temp.next
                    return
        # ---ITERATE FOR END---

        if not temp:
            # If it passed the last interval, end > the last interval's end
            # So we have to extend the last interval's end time
            prev.end = end

    def add_to_bst(self, start, end):
        if not self.BST:
            self.BST = BNode(start, end)
            return

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
                raise "Logic error! A triple booking was allowed."

        if true_if_right:
            prev.right = BNode(start, end)
        else:
            prev.left = BNode(start, end)
        
# For testing
def print_ll(ll):
    t = ll
    while t:
        print(f'({t.start}-{t.end}) -> ',end='')
        t = t.next
    print()

def print_bst(node):
    if not node:
        return
    q = deque([node])
    vals = []
    while q:
        for i in range(len(q)):
            curr = q.popleft()
            vals.append((curr.start, curr.end))
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        vals.append('|')
    print(vals)
    
# BST Node
class BNode:
    def __init__(self, start, end, left=None, right=None):
        self.start: int = start
        self.end: int = end
        self.left: 'BNode' = left
        self.right: 'BNode' = right

# Linked List Node
class LNode:
    def __init__(self, start, end, next=None):
        self.start: int = start
        self.end: int = end
        self.next: 'LNode' = next


# Your MyCalendarTwo object wiLL be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

'''
Test cases
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[80,90],[50,60],[100,110],[105,120],[20,60],[20,50]]
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[80,90],[50,60],[100,110],[60,79],[20,60],[20,50]]
["MyCalendarTwo","book","book","book","book","book","book"]
[[],[50,60],[20,30],[100,110],[61,70],[10,20],[33,40]]
["MyCalendarTwo","book","book","book","book","book","book","book","book"]
[[],[0,10],[20,30],[40,60],[70,80],[90,100],[110,130],[150,160],[35,105]]  # the one i worked on
'''


'''
Solution written after seeing the editorial
Beats 18% in runtime (~1230 ms)
'''
class MyCalendarTwo:
    def __init__(self):
        self.meetings = []
        self.double_intervals = []

    def book(self, start: int, end: int) -> bool:
        # Check for triple overlaps
        for ms, me in self.double_intervals:
            overlap = self.get_overlap(ms, me, start, end)
            if overlap:
                return False

        # Check for new double overlaps
        for ms, me in self.meetings: 
            overlap = self.get_overlap(ms, me, start, end)
            if overlap:
                self.double_intervals.append(overlap)

        # Book the new meeting
        self.meetings.append([start, end])
        return True

    def get_overlap(self, a_left, a_right, b_left, b_right):
        start = max(a_left, b_left)
        end = min(a_right, b_right)
        if start < end:
            return [start, end]
        return None    

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
