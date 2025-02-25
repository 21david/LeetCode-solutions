"""
If we traverse from left to right, when we find an odd number, it makes a 
subarray with every even number to its left before hitting an odd number. 
Say we reached 11 in this array:
(x denotes odd numbers)
        x     x
0 2 2 2 5 2 4 11
          |---|  = 3 odd subarrays [[11], [4,11], [2,4,11]]

but if there are more odd numbers even further to the left, it makes more 
odd subarrays:
    x     x       x         x     x
0 2 1 0 2 3 2 4 8 7 0 2 2 2 5 2 4 11
|---|       |-----|           |---| = 10 odd subarrays ending at 11. 
    [[7 to 11], [8 to 11], [4 to 11], ...]

for each number, we calculate how many subarrays we can form and add 
to the final answer. We can do this easily by storing the running totals, 
keeping a count variable that counts how many even numbers we've 
traversed in a row, and a boolean flag that tells us which group we're 
working on. There are two groups that will alternate, so we keep 2 running
totals and switch every time we find an odd number:
    x     x       x         x     x
0 2 1 0 2 3 2 4 8 7 0 2 2 2 5 2 4 11
|---|       |-----|           |---| 
      |---|         |-------|


TC: O(N)
SC: O(1)
"""
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = (10 ** 9 + 7)
        group_a = group_b = 0
        flag = True
        count = 0
        answer = 0
        for num in arr:
            count += 1
            if num & 1:  # Odd numbers
                if flag:
                    group_a += count
                    answer += group_a
                else:
                    group_b += count
                    answer += group_b

                count = 0
                flag = not flag
            else:  # Even numbers
                if flag:
                    answer += group_b
                else:
                    answer += group_a

            answer %= MOD

        return answer
