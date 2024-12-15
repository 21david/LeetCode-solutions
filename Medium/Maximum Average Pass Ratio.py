'''
After seeing all hints

TC: O(E log N + N). 
    O(N) for building the changes array and heapifying it. 
    O(E log N) for distributing students.
SC: O(N) for the heap
E = extraStudents
N = number of classes
'''
from heapq import heapify, heappop as pop, heappush as push
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
      # Sort heap by classes that would get the biggest change with 1 passing student
        changes = [
            [-(((pair[0]+1) / (pair[1]+1)) - (pair[0] / pair[1])), idx] 
            for idx, pair in enumerate(classes)
        ]
        heapify(changes)

        # Distribute the students optimally
        while (extraStudents := extraStudents - 1) >= 0:
            biggest_change, idx = pop(changes)

            # Add student to class i
            classes[idx][0] += 1
            classes[idx][1] += 1

            # Push back in case we want to add another student to this class again
            passing, total = classes[idx]
            push(changes, [-(((passing+1) / (total+1)) - (passing / total)), idx])


        # Return the new average
        return sum(passing / total for passing, total in classes) / len(classes)
