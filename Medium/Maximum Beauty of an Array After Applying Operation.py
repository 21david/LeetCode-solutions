'''
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation

High level steps:
1. Create sorted array of all the starts and ends of each number's range.
2. Sweep through the array, keeping track of the maximum number of ranges that
   overlap at any time.
3. Return this number.

Line sweep algorithm detailed:
1. Create an array with the start and end of each interval (length 2*N). Sort it
   in ascending order with ends coming after starts for ties. This can be done by
   adding tuples, where the second element is False (or 0) if it is a start, or 
   True (or 1) if it is an end. Then sorting will put the ends after the starts 
   if they overlap.
2. Do a linear "Sweep" through this array. For every start, add one to the count,
   and for the end, remove one from the count. Record the highest amount of intervals
   that overlapped (highest value of the count), because this represents a value
   (or sub interval of values) that each of those numbers can be changed to.

TC: O(NlogN) because of the sorting
SC: O(N) for the sorting in Python and for the sorted array
'''
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        array = []
        for num in nums:
            array.append((num - k, 1))  # Start of a range
            array.append((num + k + 1, -1))  # End of a range. Add 1 to make it overlap with tieing starts.

        array.sort()

        overlapping = 0
        max_overlaps = 0
        for _, val in array:
            overlapping += val
            max_overlaps = max(max_overlaps, overlapping)

        return max_overlaps


'''
Linear solution after seeing the editorial:
Line Sweep / Prefix Sum approach, without sorting
1. Create an array of length (max_value - min_value), called count
2. For each number, add 1 to the index that represents it's start 
   (use index 0 if it would be a negative index), and subtract 1
   to the index after the one that represents it's end (so that tieing
   starts and ends count as overlapping. If it goes past the last index,
   it can be ignored since intervals past the last number can't be greater).
3. Using this array, find the maximum number of overlaps for any number, 
   which represents the maximum frequency for that number. Traverse the array
   and add the values to a variable that stores the current sum, as if 
   creating a prefix sum array.

TC: O(N + maxVal - minVal) 
SC: O(maxVal - minVal) 
'''
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        # Find min and max values
        max_val, min_val = max(nums), min(nums)

        # Create array that tells us number of range starts and ends at each number
        # from min_val to max_val
        count = [0] * (max_val - min_val + 1)
        for num in nums:
            num -= min_val  # Adjust it to represent the right index in the array

            # Increment index of the start of the interval by 1, 
            # or index 0 if it's earlier than the min_val
            count[max(num - k, 0)] += 1

            # Increment the index after the end of the interval by 1,
            # only if it is in bounds. Otherwise, there's no need to update anything,
            # since the intervals that exceed the last index will never be greater.
            if num + k + 1 < len(count):
                count[num + k + 1] -= 1

        # Find the maximum number of overlaps at any index (line sweep)
        current_sum = 0
        max_beauty = 0
        for val in count:
            current_sum += val
            max_beauty = max(max_beauty, current_sum)

        return max_beauty

        
