"""
https://leetcode.com/problems/product-of-array-except-self

Create a "prefix product" array for all numbers to the left of an index.
Then another one for all numbers to the right of an index.
Both O(N). Then just multiply the numbers at each index to get the answer.

[2,  3,  4, 5] = nums

[1,  2,  6, 24] = left products
[60, 20, 5, 1]  = right products

[60, 40, 30, 24] = answer

TC: O(N)
Auxiliary SC: O(N)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_left = [1]
        for i in range(len(nums) - 1):
            prefix_left.append(prefix_left[-1] * nums[i])

        prefix_right = [1]
        for i in range(len(nums)-1, 0, -1):
            prefix_right.append(prefix_right[-1] * nums[i])
        prefix_right.reverse()

        answer = []
        for i in range(len(nums)):
            answer.append(prefix_left[i] * prefix_right[i])

        return answer


"""
Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)

The same process can be followed by using the left prefix product array as the
final array. After calculating the products of all left numbers at each index,
we traverse the nums array from right to left, calculating the sum in a variable
'product'. Then at each index, we just multiply the number by product, which 
stores a cumulative product of numbers in nums going from right to left.

[2,  3,  4, 5] = nums

[1,  2,  6, 24] = answer  (prefix product array)

[60, 40, 30, 24] = answer  (multiplied by cumulative product of nums going from right to left)

TC: O(N)
Auxiliary SC: O(1)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # For each index, get the product of all numbers to the left (out of bounds = 1)
        # (Like building prefix sum but with multiplication)
        answer = [1]
        for i in range(len(nums) - 1):
            answer.append(answer[-1] * nums[i])

        # Get the cumulative product going from right to left now
        # And multiply the numbers by that
        product = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= product
            product *= nums[i]

        return answer
