class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        # Sieve of erathosthenes
        prime = [True] * (n+1)
        p = 2
        while p*p <= n:
            if prime[p]:
                i = p*p
                while i <= n:
                    prime[i] = False
                    i += p
            p += 1

        # Greedily take the smallest numbers until sum would exceed s
        total_sum = 0
        answer = []
        for num in range(2, len(prime)):
            if prime[num]:
                if total_sum + num <= s:
                    total_sum += num
                    answer.append(num)
                else:
                    break

        return answer
