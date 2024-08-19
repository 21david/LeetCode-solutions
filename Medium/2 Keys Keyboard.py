'''
I thought of this algorithm by playing around with the factors of each input
and putting several examples through the test cases to see the expected values.
In the best way I can word it:
I found that for each number, you want to take it's highest divisor, because that
minimizes the number of operations to build the number since the other divisor will
be its lowest divisor. (Example, for 24, take 12, because it would take only 2 operations
to build 24.) I hypothesized that if you can find out how to build 12 with the lowest
number of operations, then that would be used in finding the minimum number of 
operations to build 24. So therefore, you would repeat the process with 12 (2 * 6),
which repeats the process with 6 (2 * 3). 3 is a prime number, which produces a
greatest divisor of 1, so from there, you would start to build the original number
in the minimal way.
This was sort of an educated guess approach. I wasn't sure it worked until I ran it.
A better way may be to find the lowest divisor of a number, which gives you the
highest divisor just by dividing N by it.

Part A
Divide the number by 2. If this number divides N with 0 remainder, we'll continue.
In other words, if N is divisible by this number.
If not, subtract 1 and check if it divides N.
Basically, this finds the biggest integer that N is divisible by.
Example: 12 for 24, 5 for 25, 1 for 19 (and every other prime number), 7 for 21

If we repeat this, we will have gone through a set of numbers, and the last one will
be a prime number.

Example: 36 -> 18 -> 9 -> 3


Part B
At that point, we can start building the answer.
Starting with the prime number, we will calculate how to build each number
in the minimum amount of steps.

For 36, the min would be 10:
(C = copy, P = Paste)
1. build 3
    C P P
    This is the shortest way to make 3 because it's a prime number
2. Using the shortest way to build 3, build 9 in the shortest way. We need 3 more operations
    because 9 / 3 = 3
    (C P P) C P P
    This should be the shortest way to make 9
3. Using the shortest way to build 9, build 18
    We need 2 more operations because 18 / 9 = 2
    (C P P C P P) C P
4. And so forth
    We need 2 more operations because 36 / 18 = 2
    (C P P C P P C P) C P

So we just need to count how many operations we need to do and return that.
'''

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1: return 0
        
        # Get the divisor as explained above
        def greatest_divisor(n):
            greatest_divisor = n // 2
            while n % greatest_divisor:
                greatest_divisor -= 1
            return greatest_divisor

        # Get all the divisors
        arr = []
        divisor = n
        while divisor != 1:
            arr.append(divisor)
            divisor = greatest_divisor(divisor)

        # Initialize total with the prime number
        # Which represents copying and pasting the single A to get that many As
        total = arr[-1]
        # For every divisor we found, add the operations it adds
        # Each of these operations is the minimum way to build the next number, until reaching N
        for i in range(len(arr)-2, -1, -1):
            total += arr[i] // arr[i+1]    

        return total


'''
An alternate way to find the greatest divisor
Which starts at 2 and find the lowest divisor,
then just divides the number by that to get
the greatest divisor.
'''
def greatest_divisor(n):
    greatest_divisor = 2
    while n % greatest_divisor:
        greatest_divisor += 1
        if greatest_divisor > n / 2:  # prime numbers will get caught here
            return 1
    return n // greatest_divisor
