# https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special

class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        Mathematically, these 'special numbers' happen to 
        be squares of prime number. So if a number is prime,
        its square is a special number. Therefore, a good
        solution is:
        Find the sqrt of l and r.
        Do sieve of erathosthenes from 0 to r.
        Quickly count how many primes are from l to r.
        That amount is equivalent to the number of special
        number from l to r. Subtract that from the amount
        of numbers from l to r to get the number of NOT 
        special numbers, and return the result.
        """
        l_orig = l
        r_orig = r

        l = int(ceil(sqrt(l)))
        r = int(sqrt(r))

        is_prime = [True] * (r+1)
        is_prime[0] = is_prime[1] = False

        for n in range (2, int(sqrt(r))+1):
            t = n * 2  # start at the next multiple of the current number
            while t <= r:  # while t in bounds of the array
                is_prime[t] = False  # mark all multiples as not prime nums
                t += n  # move to the next multiple

        total_nums = (r_orig - l_orig + 1)
        num_of_special_nums = len([x for x in is_prime[l:] if x])
        return total_nums - num_of_special_nums
