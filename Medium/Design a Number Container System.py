# Dictionaries + SortedList
from sortedcontainers import SortedList
class NumberContainers:
    # O(1)
    def __init__(self):
        self.num_at_idx = defaultdict(int)  # stores { idx : number }
        self.sorted_indices = defaultdict(SortedList)  # stores { number : [sorted list of its indices] }

    # O(logN)
    def change(self, index: int, number: int) -> None:
        # If we are changing a value, take care of the old info
        old_num = self.num_at_idx[index]
        if old_num:
            self.sorted_indices[old_num].remove(index)  # O(log N)
            if len(self.sorted_indices[old_num]) == 0:
                del self.sorted_indices[old_num]

        # Add new number to dictionaries
        self.num_at_idx[index] = number
        self.sorted_indices[number].add(index)  # O(log N)

    # O(1)
    def find(self, number: int) -> int:
        if number in self.sorted_indices:
            return self.sorted_indices[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
