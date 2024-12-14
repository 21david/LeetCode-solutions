'''
https://leetcode.com/problems/wiggle-sort-ii/

An O(N) TC / O(N) SC approach with counting sort.
Get the max and min element, then create an array that spans [min, max].
Get a count of each number. Then sort the numbers.

Since we may have an input like [1, 1, 2, 2, 2, 2, 3, 3], we can't just take 
from the left and right repeatedly until meeting in the middle, because we
would get [1, 3, 1, 3, 2, 2, 2, 2]. But we can take set a pointer to the
start, and a pointer to the middle, take from each, and push each to the right
by 1. I think its guaranteed that arr[i] < arr[j] like this.

The code needs to handle even and odd length arrays too.

No hints or anything used, except seeing counting sort explanation. Solved after solving the first one.
'''
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Counting sort
        biggest = max(nums)
        smallest = min(nums)
        counts = [0] * (biggest - smallest + 1)
        for num in nums:
            counts[num - smallest] += 1
        sorted = []
        for idx, count in enumerate(counts):
            # idx + smallest = the number represented
            sorted.extend([idx + smallest] * count)

        # In place wiggle sort by using the sorted array with two pointers
        N = len(nums)
        j = N // 2 - (N % 2 == 0)
        i = 0
        while j >= 0:
            nums[i] = sorted[j]
            if i + 1 < N:
                nums[i+1] = sorted[j + N // 2]

            j -= 1
            i += 2
