class Solution:
    def splitArray(self, nums: List[int]) -> int:
        primes = nonprimes = 0

        # Sieve of Eratosthenes
        n = len(nums) + 1
        prime = [True] * (n+1)
        prime[1] = prime[0] = False
        p = 2
        while p * p <= n:
            if prime[p]:
                i = p * p
                while i <= n:
                    prime[i] = False
                    i += p
            p += 1

        # Calculate sums based on the primality of the index
        for i in range(n-1):
            if prime[i]:
                primes += nums[i]
            else:
                nonprimes += nums[i]

        return abs(primes - nonprimes)
