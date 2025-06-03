# https://leetcode.com/problems/target-sum

'''
Recursive solution
TLE 79/140
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # at index i with total sum of x, we want to know in how many ways its possible
        # to sum to the target using the rest of the array.
        def find(i, so_far):
            if i == len(nums):
                return int(so_far == target)

            ways1 = find(i+1, so_far + nums[i])
            ways2 = find(i+1, so_far + -nums[i])

            return ways1 + ways2

        ans = find(0, 0)
        return ans 


'''
Recursive, memoized with a dictionary

The brute force and simpler approach is to try every combination of -s and +s
and check which ones sum to the target. This would be O(2^N) time complexity.

Memmoization:
At index i with total sum of x, we want to know in how many ways its possible
to sum to the target using the rest of the array. 
because at index i with a sum of x, there may be multiple combinations using 
the first i numbers that sum to x. So if we memoize, if we reach a second
combination (and any more after that) that give the same sum at index i as
a previous sum, then the answer will be the exact same and we can just
use the memoized value instead of trying every combination again.
Example:
+2, -1, -2,  4, 5, 6
-2, -1, +2,  4, 5, 6
         i

If we get to position i, on the second combination, it also sums to -1. So answering
"can we use the rest of the numbers + -1 to sum to the target" will be the same, therefore
we can memoize. This would save more and more time as the combinations grow larger.

More examples:
-1, -2, 3,  4, 5, 6
 1, 2, -3,  4, 5, 6
        i

 1, 2, 3, 4, -5,   6
1, -2, -3, 4, 5,   6
              i
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def find(i, so_far):
            if i == len(nums):
                return int(so_far == target)
            elif (i, so_far) in memo:
                return memo[(i, so_far)]

            ways1 = find(i+1, so_far + nums[i])
            ways2 = find(i+1, so_far + -nums[i])

            ans = ways1 + ways2
            memo[(i, so_far)] = ans
            return ans

        return find(0, 0) 


'''
Recursive, memoized with @cache
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def find(i, so_far):
            if i == len(nums):
                return int(so_far == target)

            ways1 = find(i+1, so_far + nums[i])
            ways2 = find(i+1, so_far + -nums[i])

            return ways1 + ways2

        ans = find(0, 0)
        return ans 


'''
1-line recursive memoized, for fun
'''
# 1 line recursive
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return (find := cache(lambda i, so_far: so_far == target if i == len(nums) else find(i+1, so_far + nums[i]) + find(i+1, so_far + -nums[i]))) (0, 0)


'''
2D tabulated DP
Solved after seeing only the recursive memoized editorial solution

TC: O(N * T)
SC: O(N * T)
where T is the total sum of all numbers in nums, and N is the length of nums

dp[i][left] = dp[i+1][left + nums[i]] + dp[i+1][left - nums[i]]
base case: dp[len(nums)][total_sum] = 1
This represents "amount_left" is 0 when all numbers are used
The answer should be in dp[0][total_sum + target]

I derived this by first making a recurrence relation from the recursive solution, and thinking
what the dimensions meant (i and left) and what the base case was. If you start with the target
and subtract from it to try to get to 0, then that means that when the "amount_left" is 0, you 
have found 1 way. I drew out the DP table and thought about how the solution could be derived.
I tried to apply the recurrence relation until I found a pattern that seemed to get the solution.
And testing it on various examples, it made a lot of sense and worked for all of them. The pattern
is to start at the base case, which is the 1 that is set initially, and then move up to the previous
row, then 1) move left nums[i] spots, and add the current value to that spot, 2) do the same but
moving right nums[i] spots. This is basically what the recursive version is doing.
Then once I knew the pattern well, I implemented it. An observation is that the answer seems to
be the same from whichever direction you do the problem in: left to right or right to left.
So I think the DP could also be done in multiple ways: width and height can be swapped,
problem can be done from the top row to the bottom or the bottom to the top.
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0

        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums) + 1)]
        dp[len(nums)][total_sum] = 1

        # Solving from bottom row to top
        for row_num in range(len(nums), 0, -1):
            for idx, ele in enumerate(dp[row_num]):
                if ele:
                    dp[row_num-1][idx + nums[row_num-1]] += dp[row_num][idx]
                    dp[row_num-1][idx - nums[row_num-1]] += dp[row_num][idx]

        return dp[0][total_sum + target]


'''
1D tabulated DP

Solved by thinking about the approach used in the 2D version.
But this time in a different order (top row to bottom row).
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0

        dp = [[0] * (2 * total_sum + 1)] + [[0] * (2 * total_sum + 1)]
        dp[0][total_sum] = 1

        # Solving from top row to bottom row, 1D DP
        for num in nums:
            for idx, ele in enumerate(dp[0]):  # idx represents current sum I believe
                if ele:
                    dp[1][idx + num] += dp[0][idx]
                    dp[1][idx - num] += dp[0][idx]
                    dp[0][idx] = 0
            dp[0], dp[1] = dp[1], dp[0]

        return dp[0][total_sum + target]
