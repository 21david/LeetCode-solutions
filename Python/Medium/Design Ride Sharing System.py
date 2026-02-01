'''
DLL data structure:
A dictionary that maps an id to a Node
The Nodes are in a doubly linked list that behaves like a queue
There is a dummy start and end node to make it easier to insert and remove nodes


Dictionary:        {  3,      1  }    # ids of riders (and the other one stores drivers), 'ids' in the code
                      |       |
Linked List: [X] <-> [3] <-> [1] <-> [X]    # also ids of riders/drivers.  start with 'start', and 'end' (dummy nodes) in the code
'''

class RideSharingSystem:

    def __init__(self):
        self.riders = DLL()
        self.drivers = DLL()
        

    def addRider(self, riderId: int) -> None:
        self.riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.add(driverId)
        

    def matchDriverWithRider(self) -> List[int]:
        # Take from the start of both DLLs
        rider = self.riders.get_first()
        driver = self.drivers.get_first()

        if rider is not None and driver is not None:
            answer = [driver, rider]

            # Delete them
            self.riders.remove(rider)
            self.drivers.remove(driver)

            return answer
        else:
            return [-1,-1]
        

    def cancelRider(self, riderId: int) -> None:
        self.riders.remove(riderId)
        # return None
        
class DLL:  # dictionary with doubly linked list
    def __init__(self):
        self.ids = {}
        self.start = Node(None)
        self.end = Node(None)

        self.start.right = self.end
        self.end.left = self.start

    def add(self, id: int):
        # Create node
        newp = Node(id)  # new person

        # Insert node to the right
        prev = self.end.left
        newp.left = prev
        newp.right = self.end
        prev.right = newp
        self.end.left = newp

        # Create dictionary mapping
        self.ids[id] = newp

    def remove(self, id: int):
        if id not in self.ids:
            return
            
        delNode = self.ids[id]
        del self.ids[id]

        prev = delNode.left
        next = delNode.right

        prev.right = delNode.right
        next.left = delNode.left

        # not sure if needed:
        delNode.left = None
        delNode.right = None

    def get_first(self):
        return self.start.right.id
        

class Node:
    def __init__(self, id):
        self.left = None
        self.right = None
        self.id = id

# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)©leetcode
