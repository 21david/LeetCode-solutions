"""
Quick select:
The idea is to reorder the array such that pivot_dist is in its final
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

Space complexity: O(1)
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
