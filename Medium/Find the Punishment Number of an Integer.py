# Actual algorithm
class Solution:
    def punishmentNumber(self, N: int) -> int:
        # Finds whether a number can be partitioned as described in the problem
        def can_partition(num):
            def helper(acc, n):
                if n <= 10:
                    return acc + n == num

                ans = False
                div = 10
                while (n * 10) // div:
                    ans |= helper(acc + n % div, n // div)
                    div *= 10

                return ans

            return helper(0, num**2)

        # Go through each number and add the squares of the numbers
        # that can be partitioned to the answer
        ans = 0
        for n in range(1, N + 1):
            if can_partition(n):
                ans += n ** 2

        return ans
