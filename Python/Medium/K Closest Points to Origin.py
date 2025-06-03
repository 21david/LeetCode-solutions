"""
Quick select:
The idea is to reorder the array such that the pivot is in its final
place, which is the exact place it would be in if the array was sorted,
and have all the elements before it be ≤ it, and all the elements after
it be > it. We can know the closest k points only when the final index 
of pivot_dist is either k or k + 1.

k or k + 1 both work because the pivot always gets swapped into its
sorted position after a partition, which is at index 'wall - 1'.
So everything to the left of the pivot will be ≤ it. 
The algorithm stops when elements 0 to k - 1 are guaranteed to have
the smallest k elements.
If it lands on k, the pivot will be on index k-1, and everything to the
left will be smaller. Taking the elements at indices 0 to k - 1 would
give the answer. In this case, the pivot would be the last element
in the k closest elements, assuming distinct numbers.
If it lands on k + 1, the pivot will be on index k, and everything to the
left will be smaller, which would still guarantee that the smallest k
elements are on indices 0 to k - 1. In this case, the pivot would
be the first element after the k closest elements, assuming distinct 
numbers.

Time complexity:
    Average: O(N)
    Worst: O(N^2)

Space complexity: O(N) due to recursion call stack
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(point):
            return point[0] ** 2 + point[1] ** 2

        def quick_select(start, end):
            # Pick random pivot and then swap it to the beginning
            randIdx = random.randint(start, end - 1)
            points[start], points[randIdx] = points[randIdx], points[start]
            pivot_dist = get_dist(points[start])

            # Lomuto's partitioning algorithm
            wall = start  # behind this 'wall', all elements are ≤ pivot
            for i in range(start, end):
                if get_dist(points[i]) <= pivot_dist:
                    points[wall], points[i] = points[i], points[wall]
                    wall += 1

            points[start], points[wall-1] = points[wall-1], points[start]

            # Everything at position 'wall-1' and before is ≤ pivot_dist
            if wall in (k, k+1):
                return  # Smallest k elements should be in points[:k] already
            elif wall < k:
                quick_select(wall, i + 1)  # Go right
            else:
                quick_select(start, wall - 1)  # Go left

        quick_select(0, len(points))

        return points[:k]



"""
Optimized quick select using three way partitioning from 75. Sort Colors

Time complexity:
    Average: O(N)
    Worst: O(N^2)

Space complexity: O(1)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(point):
            return point[0] ** 2 + point[1] ** 2

        # Quick select
        left, right = 0, len(points) - 1
        while True:
            pivot_idx = random.randint(left, right)
            pivot = points[pivot_idx]
            pivot_dist = get_dist(pivot)

            lesserIdx = left  # every element behind is > pivot
            eqIdx = left  # every element after and including lesserIdx and behind eqIdx is = pivot

            # Sorting algorithm from Sort Colors / Dutch National Flag problem
            for i in range(left, right + 1):
                dist = get_dist(points[i])
                if dist < pivot_dist:
                    temp = points[i]
                    points[i] = points[eqIdx]
                    points[eqIdx] = points[lesserIdx]
                    points[lesserIdx] = temp
                    lesserIdx += 1
                    eqIdx += 1
                elif dist == pivot_dist:
                    points[i], points[eqIdx] = points[eqIdx], points[i]
                    eqIdx += 1

            # Elements at indices 'lesserIdx' to 'eqIdx - 1' are all = to pivot 
            # and are in their final sorted positions. If k falls in this range
            # then the answer is everything before index k. 
            # Else, repeat on the left or the right depending on where k is.
            if lesserIdx <= k <= eqIdx:
                return points[:k]
            elif k < lesserIdx:
                right = lesserIdx - 1
            else:
                left = eqIdx
    
