# https://leetcode.com/problems/all-oone-data-structure/

# Linked List Node
class LNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.set = set()

class AllOne:
    def __init__(self):
        self.map = {}
        self.left = LNode()
        self.right = LNode(prev=self.left)
        self.left.next = self.right

    def inc(self, key: str) -> None:
        if key not in self.map:
            # Check if node for frequency 1 exists
            if self.left.next.val == 1:
                # If it exists, get it
                freq_1_node = self.left.next
            else:
                # If not, create it and insert it
                freq_1_node = LNode(1, prev=self.left)
                next = self.left.next
                next.prev = freq_1_node
                self.left.next = freq_1_node
                freq_1_node.next = next

            freq_1_node.set.add(key)
            self.map[key] = freq_1_node

        else:
            freq_node = self.map[key]
            freq_val = freq_node.val

            # Check if there is a node for the next frequency (ex. 1 -> 2)
            if freq_node.next.val == freq_val + 1:
                # Just move it to the next node
                freq_node.set.remove(key)
                freq_node.next.set.add(key)
            
            # If there isn't a node
            else:
                # Create it and insert it
                new_freq_node = LNode(freq_val + 1)
                new_freq_node.prev = freq_node
                new_freq_node.next = freq_node.next
                freq_node.next.prev = new_freq_node
                freq_node.next = new_freq_node

                freq_node.set.remove(key)
                freq_node.next.set.add(key)
            
            # Update pointer in the map
            self.map[key] = freq_node.next

            # Delete freq_node if it has no more keys
            if len(freq_node.set) == 0:
                freq_node.prev.next = freq_node.next
                freq_node.next.prev = freq_node.prev
                freq_node.prev = None
                freq_node.next = None
                del freq_node  # ?

    def dec(self, key: str) -> None:
        if key not in self.map:
            return

        freq_node = self.map[key]
        
        # Check if it its frequency is 1
        freq_val = freq_node.val
        if freq_val == 1:
            # If it is, delete it
            freq_node.set.remove(key)
            del self.map[key]
        
        # If it has a frequency >= 2, move to another node
        else:
            # Check if there is a node for the prev frequency (ex. 2 -> 1)
            if freq_node.prev.val == freq_val - 1:
                # Just move it
                freq_node.set.remove(key)
                freq_node.prev.set.add(key)
            else:
                # If there is no node for the prev frequency, create and insert it
                new_freq_node = LNode(freq_val - 1)
                new_freq_node.prev = freq_node.prev
                new_freq_node.next = freq_node
                freq_node.prev.next = new_freq_node
                freq_node.prev = new_freq_node

                freq_node.set.remove(key)
                freq_node.prev.set.add(key)

            # Update pointer in the map
            self.map[key] = freq_node.prev

        # Delete freq_node if it has no more keys
        if len(freq_node.set) == 0:
            freq_node.prev.next = freq_node.next
            freq_node.next.prev = freq_node.prev
            freq_node.prev = None
            freq_node.next = None
            del freq_node  # ?

    def getMaxKey(self) -> str:
        max_node = self.right.prev
        if max_node.val is not None:
            return next(iter(max_node.set))
        else:
            return ''
        
    def getMinKey(self) -> str:
        min_node = self.left.next
        if min_node.val is not None:
            return next(iter(min_node.set))
        else:
            return ''

# For testing
def print_linked_list(l):
    while l:
        print(l.val,  f'({l.set})', end=' -> ')
        l = l.next
    print('X')    


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

'''
Attempted after seeing Editorial but not seeing the code.
Approach:
1) Dictionary/Map of [string] -> [node_pointer]
    - Each input string gets stored, and it points to a node
    that has its frequency
2) Doubly linked list
    - Each node stores an integer which represents a frequency
    and a set, which stores all the keys with that frequency
    - Dummy left and right nodes make this much easier

When adding a new key, check if a node for frequency 1 exists (start at
left dummy node and check the one to the right of it). If it doesn't, 
create the node, insert it at that position, and add the key to its set.
Then add the key to the dictionary along with a pointer to that node.
When incrementing an existing key, get a pointer to its node. Check if
the node to the right of that node is 1 greater than the current node.
If it is, just remove the key from the current set and put it in the next
node's set. If it isn't, we need to create a new node, insert it, and then
move the current key to that new node. After doing either of the above,
we need to check if we removed the last key from the node. If we did, then
we have to delete it by rewiring the linked list nodes. If we didn't, we
can just leave it.
This will make it such that there are only nodes for existing frequencies
(such as 1, 5, etc), and they will all be in line and in order. To get the
min or the max, we just start at either the left or the right dummy nodes,
move to the adjacent node, and return any key from its set. 
The logic for decrementing is very similar. If we are removing a key that
had a frequency of 1, then we delete it from the set. If we are removing
a key that had a frequency of at least 2, then we try moving it to the
node to the left, which will similarly result in either using the node
that was already there or creating and inserting a new one. And then we check
if we removed the last key in a node and either delete that node or leave it.
Everything does constant work.
TC for each function: O(1)
SC for each function: O(1)
SC for the class object: O(N), where N is the number of keys.
'''
