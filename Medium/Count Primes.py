# https://leetcode.com/problems/count-primes

class Solution(object):
    def countPrimes(self, num):
        """
        :type n: int
        :rtype: int
        """
        """
        Sieve of Eratosthenes approach.
        """
        if num <= 1:
            return 0

        is_prime = [True] * (num)
        is_prime[0] = is_prime[1] = False

        for n in range (2, int(sqrt(num))+1):
            if not is_prime[n]:
                continue
            t = n * n  # start at the first multiple that may not have been marked
            while t < num:  # while t in bounds of the array
                is_prime[t] = False  # mark all multiples as not prime nums
                t += n  # move to the next multiple

        return is_prime.count(True)
