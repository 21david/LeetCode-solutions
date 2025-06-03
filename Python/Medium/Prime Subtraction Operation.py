'''
https://leetcode.com/problems/prime-subtraction-operation

Greedy:
Go from right to left. 
When an i is found such that nums[i] >= nums[i+1],
subtract the smallest prime number that will make
nums[i] < nums[i+1].
Repeat for all i, and return false if a pair is found that
can't begfdsgfds fixed, or true if it makes it to the begining of the array.

To find the smallest prime number that will fix a pair, I think
we can do a binary search on a list of prime numbers.
Since the constraints are small, we could import all prime numbers
< 1000. If they weren't small, we could either find the largest number
in nums, and make a list of all prime numbers < that number,
or dynamically increase the list of prime numbers as needed (probably more
efficient.)

Another approach is to calculate the amount needed to subtract from nums[i] to
make it < nums[i+1], then find the least prime number that is >= that number.
For that, a pre-declared set of prime numbers would work, or it could try to
mathematically find it by checking and incrementing repeatedly.

Optimization: Most minimum array would be [1, 2, 3, 4, ...]
So for each element, check that it is at least (i+1) if i is the index.
'''
primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 
        239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
        331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 
        509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 
        613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
        709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 
        821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 
        919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009
    ]

# It may be better to use a set, but im writing a BS for practice
def binary_search(target):
    lo = 0
    hi = len(primes) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if primes[mid] == target:
            return target
        elif primes[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    # If it didn't find it, we need to return the next greatest one
    while primes[mid] < target:
        mid += 1

    return primes[mid]

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if nums[-1] < len(nums):
            return False

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < i + 1:  # Optimization
                return False

            if nums[i] >= nums[i+1]:
                diff = nums[i] - nums[i+1] + 1
                # Goal is to subtract at least diff from nums[i] to make it less than nums[i+1]
                nums[i] -= binary_search(diff)
                if i >= 1 and nums[i] <= 1:
                    # Next pair won't be fixable because the lowest number (1) was already reached
                    return False
        
        if nums[0] < 1:
            return False

        return True
