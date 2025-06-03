'''
https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c
See my solution post here: https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/solutions/5778109/one-line-math-solution-different-from-editorial/
'''

'''
Some observations:
In the binary representation of a and b:
Two 1s need to be a 0 => 2 flips
0 and 1 need to be a 0 => 1 flip
Two 0s need to have at least one 1 => 1 flip
0 and 1 need to be a 1 => 0 flips
Both bits are already the same as in c => 0 flips
'''
'''
Solution with a loop:
Iterate through each bit in a, b, and c at the same time.
Depending on the value of the bit in c, make the minimum adjustments
in a and/or b:
Pseudocode:
    count = 0
    for all bits in a, b, and c
        if c == 1
            if a and b are 0, add 1 to count
        if c == 0
            if a and b are both 1, add 2 to count
            if a and b sum to 1, add 1 to count
    return count
A couple of bit/math tricks can shorten this code
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if c_bit:
                count += 1 - (a_bit | b_bit)
            else:
                count += a_bit + b_bit
            
            a >>= 1
            b >>= 1
            c >>= 1

        return count


'''
One-line loop solution
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return sum(1 - ((a | b) >> p & 1) if c >> p & 1 else (a >> p & 1) + (b >> p & 1) for p in range(floor(log(max(a, b, c), 2) + 1)))


'''
Expanded version of the one above
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0

        # Get number of bits in the biggest number
        num_bits = floor(log(max(a, b, c), 2) + 1)
        
        for position in range(num_bits): 
            if c >> position & 1:
                count += 1 - ((a | b) >> position & 1)
            else:
                count += (a >> position & 1) + (b >> position & 1)

        return count
      

'''
One line math solution
'''
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((~a & ~b & c) | (a ^ b) & ~c).bit_count() + 2 * (a & b & ~c).bit_count()


'''
Another way to solve it could be like this:
Super brute force:
Attempt all combination of flips for a and b, and check if their OR result
is equal to c. Keep track of how manny flips are used in the combination
with the least number of flips.
'''
