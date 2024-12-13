'''
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements

1. Put all elements into a doubly linked list, so that each one can access its neighbors
2. Put each node into an array and sort by value
3. From smallest to largest, pick each node and mark its neighbors. Skip marked nodes.
4. Return the sum of all picked nodes.

TC: O(NlogN) for sorting
SC: O(N) for the linked list and array
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Build doubly linked list
        head = Node(nums[0])
        prev = head
        node_arr = [head]
        for i in range(1, len(nums)):
            node = Node(nums[i])
            node.prev = prev
            prev.next = node
            prev = node
            node_arr.append(node)

        # Sort by node values
        node_arr.sort(key = lambda node: node.val)
        
        # Traverse from smallest to largest, marking neighbors, and skipping marked nodes
        answer = 0
        for node in node_arr:
            if node.val is None:
                continue

            answer += node.val

            if node.prev:
                node.prev.val = None
            if node.next:
                node.next.val = None

        return answer

class Node:
    def __init__(self, v, p = None, n = None):
        self.val = v
        self.prev = p
        self.next = n

    def __repr__(self):
        return f'{self.prev.val if self.prev else "X"}<-{self.val}->{self.next.val if self.next else "X"}'



'''
After seeing solution 1 explanation in editorial

TC: O(NlogN) for sorting
SC: O(N) for the auxiliary arrays
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Sort
        nums_with_indices = [[num, idx] for idx, num in enumerate(nums)]
        nums_with_indices.sort()

        answer = 0
        for num, idx in nums_with_indices:
            if nums[idx] is not None:
                answer += num

                # Mark neighbors
                if idx - 1 >= 0:
                    nums[idx - 1] = None

                if idx + 1 < len(nums):
                    nums[idx + 1] = None

        return answer



'''
After seeing other O(N) solutions.
One-pass greedy approach. Think of the array as several strictly increasing and
decreasing subarrays put together.

An important observation is that if a number is less than both its neigbors,
it will always be picked for the sum.

For the increasing arrays, we can greedily pick the first element in it
and then every other element. Because the first element will be smaller
than the one before and after it, so it will be guaranteed to be part of
the answer (or if its the first element in the whole array).

For the decreasing arrays, we can put them in a stack as we traverse. When
we find the first element that is not strictly decreasing (that is >= prev element), 
then we know that the element right before that is a local minimum (less than
both its neighbors), and therefore needs to be part of the answer. If we 
elimnate that one, then the one right before it gets eliminated also, and the
one before that one will be the next minimum, because it has a greater element
to its left and a cancelled element to its right. So it needs to be part of
the answer and we add it. Since the array is strictly decreasing, this just
repeats for every other element every time. We essentially do the same thing 
we did for the increasing arrays, but backwards.

After processing all numbers, there may be some still in the stack, so we process
those and return the final answer.

TC: O(N). One pass through the array.
SC: O(N). For the stack.
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        N = len(nums)
        stack = []
        total = 0
        for num in nums:
            if not stack or num < stack[-1]:
                stack.append(num)
            else:
                # End of decreasing subarray
                while stack:
                    total += stack[-1]
                    stack.pop()
                    if stack:
                        stack.pop()  # Skip prev num as it will be marked

        # Remaning numbers in stack
        while stack:
            total += stack[-1]
            stack.pop()
            if stack:
                stack.pop()  # Skip prev num as it will be marked

        return total



'''
Optimization:
We can use two pointers to find the bounds of the decreasing arays instead of using
a stack. When we find it, we can create a third pointer and traverse backwards,
adding only every other element. If we just worry about decreasing arrays, then
increasing arrays will automatically be processes like in the approach above,
because increasing arrays consist of many single-element 'decreasing' arrays.

TC: O(N). One pass through the array.
SC: O(1) for the pointers.
'''
class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums.append(math.inf)  # Dummy node to process last window within the loop
        N = len(nums)
        total = 0
        l = 0
        for r in range(N):
            if l != r and nums[r] >= nums[r - 1]:
                # End of decreasing subarray
                j = r - 1  # put j on the local minimum
                while j >= l:
                    # Add every other element
                    total += nums[j]
                    j -= 2
                # Move the window
                l = r + 1

        return total

'''
Test cases:
[2,1,3,4,5,2]
[2,3,5,1,3,2]
[9,8,7,11,10,9,8,9,8,7]
[2,2,2,3,3,5,5,1,1,1,1,2,2,3,5,5,4,4,4,4,2,2,3,3,3]
[1,2,3,4,5,4,3,2,1,2,3,4,5,3,2]
[5,10,5,10,5,10,5,10]
[1,3,1,3,5,3,2,4]
'''
