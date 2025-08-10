"""  
Setup: Create the set
TC = O(log U * D), U = upper bound, D = number of digits
    Each power of 2 is calculated, the frequency of each of its digit is calculated, and a tuple is added to the set
SC = O(log U)
    One tuple of size 10 for each power of 2 (for which there are log U of)

Actual function: reorderedPowerOf2(num: int)
TC = O(D)
    Create tuple that stores frequency of each digit, then hash it to check if its in the set
SC = O(1)
"""
powers = set()
# Add all powers of 2 with sorted digits
num = 1
BOUND = 10 ** 9
while num < BOUND:
    # Count digits in num and add a tuple to the set
    count = [0] * 10
    num_copy = num
    while num_copy:
        count[num_copy % 10] += 1
        num_copy //= 10
    digit_count_tup = tuple(count)
    powers.add(digit_count_tup)

    # Move to next power of 2
    num <<= 1

class Solution:
    def reorderedPowerOf2(self, num: int) -> bool:
        # Turn n into tuple of digit counts
        count = [0] * 10
        while num:
            count[num % 10] += 1
            num //= 10
        digit_count_tup = tuple(count)
        return digit_count_tup in powers
        

"""  
Approach 1:
Generate all permutations of reordered digits. For each one, check if it is a power of 2
in O(1) by checking log(perm, 2) % 1 < 0.000000001

Should be O(D! * D) TC, where D = number of digits.
SC should be O(D) for recursive call stack of permutations algorithm.
"""
"""  
Approach 2:

Calculate all powers of 2, sort their digits, put each one into a set as a string
2147483648 => 1234446788 
...
2048 => 0248
256 => 256
16 => 16
1 => 1
Ideally, do this once for all test cases, not per test case.
TC = O((log U) * (D log D)), U = upper bound (10^9), D = max digits (9). D log D is for sorting, 
  log U is for the number of powers of two it needs to process before hitting the bound.
SC = O((log U) * D), log U powers, each D digits long

Then just sort the input digits, and check if it is in the set
TC = O(D log D)
SC = O(D), unless you can somehow sort on the input string, then use it to check the set

Optimization: instead of sorting, create a tuple with a count of each 0-9 digit. The set stores those,
then do the same for the input number and check if the equivalent tuple is in the set. This removes
D log D sorting and turns it into D, and reduces D space complexity to 1 since each tuple would be length 10.
(Implemented above.)
"""
