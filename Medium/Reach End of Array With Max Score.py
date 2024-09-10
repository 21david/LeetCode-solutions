# https://leetcode.com/problems/reach-end-of-array-with-max-score

'''
TC: O(N^2)
SC: O(N)
'''
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # Work backwards O(N^2) approach
        n = len(nums)
        maxs = [0] * n

        for i in range(n-2, -1, -1):
            maxn = nums[i]
            length = 1
            cur_num = nums[i]
            for j in range(i+1, n):
                poss = length * cur_num + maxs[j]
                length += 1
                maxn = max(maxn, poss)
            maxs[i] = maxn

        # print(maxs)
        return maxs[0]


'''
Greedy solution using monotonic stacks

TC: O(N)
SC: O(N)
'''
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        # Find the best jumps by finding the next highest number each time
        stack = [(nums[0], 0)]
        for i, n in enumerate(nums):
            if i == 0: continue
            if n > stack[-1][0]:
                stack.append((n, i))

        # Append last one since we need to jump there regardless
        stack.append((nums[-1], len(nums)-1))

        # Calculate answer with the jumps we stored in stack
        total = 0
        prev_num, prev_idx = stack[0]
        for num, curr_idx in stack[1:]:
            total += prev_num * (curr_idx - prev_idx)
            prev_num = num
            prev_idx = curr_idx

        return total


'''
Greedy solution with just an int variable and a loop

TC: O(N)
SC: O(1)
'''
'''
The formula given can be thought of as:
Pick a number and and add that to a total sum every time you move to the next number, 
starting from the first number. For every number, you can pick it, or skip it. When 
you pick a new number, that is the number that gets added to the sum every time you 
move to the next number.
When thought of like this, to get the highest possible total, it makes sense to only 
pick a number when it is greater than the previous number you picked. You only want 
to pick a number if it will increase your sum, not decrease it.
'''
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        highest_so_far = nums[0]
        total_score = 0

        for i in range(1, len(nums)):
            total_score += highest_so_far
            highest_so_far = max(highest_so_far, nums[i])

        return total_score
            
'''
Python 1-line solution
seen on LeetCode

accumulate() with the max function as an argument creates an array
with the highest value at or to the left of each index.
If we sum all of those, we get the same value as in the algorithm
above.
'''
class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        return sum(accumulate(nums[:-1], max))
