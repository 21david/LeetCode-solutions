'''
Binary search approach.
We can start with a middle element n // 2.
We can count how many elements are smaller and how many are greater than this element.
If smaller + bigger != n, then there are at least 2 of the element and we have the answer.
If not, we can use the number of smaller elements to check in which index this element
would be in if the array was sorted. If it is at an index that is smaller than or equal to its value
(using a 1-based index), then the duplicate should be to the right. If it is at an index that is
greater than its value, the duplicate should be to the left. We repeat binary search until finding it.

TC: O(N log N)
SC: O(1)
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1  # all numbers are in the range [1, n]

        lo, hi = 1, n
        while lo <= hi:
            smaller = bigger = 0
            test_num = (lo + hi) // 2

            # Scan array and count smallers and biggers
            for num in nums:
                smaller += num < test_num
                bigger += num > test_num

            if smaller + bigger < n:
                return test_num
            elif smaller + 1 <= test_num:
                lo = test_num + 1
            else:
                hi = test_num - 1
