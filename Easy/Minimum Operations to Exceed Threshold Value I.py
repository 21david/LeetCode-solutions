"""  
Rephrased question:
How many numbers are less than k?
"""


'''
Solution 1: Count numbers less than k.
TC: O(N)
SC: O(1)
'''
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(1 for num in nums if num < k)



'''
Solution 2: Heap
TC: O(NlogN)
SC: O(1) (modifies the input)
'''
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ct = 0

        while nums[0] < k:
            heapq.heappop(nums)
            ct += 1

        return ct


'''
Solution 3: Sort, then binary search for position of first number >= k
TC: O(NlogN)
SC: O(N) (due to sorting)
'''
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        return bisect.bisect_left(nums, k)
