'''
https://leetcode.com/problems/minimum-array-end

See my solution post here:
https://leetcode.com/problems/minimum-array-end/solutions/6025106/o-logx-python-solution

Explanation:

All numbers in the array need to have the same bits turned on as in x.
So the array always needs to start with x since it needs those bits turned on.
Then, the minimal way to create the array, is to start filling in any 0s in x
with incremental binary numbers (filling in only the 0s) in the
same way you would count in binary. Do this N times and return that value.
If all 0s get filled and the result is a binary number like 11111,
then you have to start adding 1s and 0s to the end, also in the way you would
count in binary. 

Filling in all the 0s in x would be one cycle. After that cycle,
you start by adding a 1 to the left. Then for the third cycle, you add a 10 (= 2 in decimal).
Then 11 (= 3), 100 (= 4), and so forth.

There is a shortcut way to do this without building an actual array.
We can calculate the length of a cycle by raising 2 to the number of 0s in x.

2 ^ (number of 0s in x).

First we need to fill in the 0s. We can take the remainder of dividing n - 1 by the cycle length,
convert that to binary, and use that combination of 1s and 0s to replace the 0s in x. 
The - 1 is so that if n lands on the last value in a cycle, it doesn't count as going into the
next cycle. For example,  if n = 4 and cycle length = 4, then the answer is in the first cycle,
not the next one.
This is because for each cycle, the combination of 1s and 0s will repeat exactly the same.
This will let us skip all the iteration and calculate the answer.

Then, we can divide n - 1 by that result to figure out how many cycles it has to go through.
If it has to go past 1 full cycle, we append a 1 to the end of the result.
If it goes past 2 full cycles, we append a 10 to the result. 3 full cycles -> 11,
4 full cycles -> 100, and so forth.

Take n = 3, x = 4 as an example:

4 in binary is 100.

The array would look like this, with binary numbers written vertically underneath.

    [4, 5, 6] 
     1  1  1
     0  0  1
     0  1  0

100 has two 0s, which we will in as if we were counting in binary. The next number
in the sequence would be 111 (7). And after that, we would run out of numbers (end of
the cycle), so the number would be 1100 (appending a new 1 to the left and restarting
the cycle).

Take n = 14, x = 4 as an example:

                     1 1 1 1   1 1 1 1
           1 1 1 1   0 0 0 0   1 1 1 1

 1 1 1 1   1 1 1 1   1 1 1 1   1 1 1 1
 0 0 1 1   0 0 1 1   0 0 1 1   0 0 1 1
 0 1 0 1   0 1 0 1   0 1 0 1   0 1 0 1
                                 ^
                                 14th number

Now the cycles are visible (separated by spaces).
For each cycle, we repeat the same combination of 1s and 0s in the first 4 bits, and we add the next 
binary number to the top (first cycle we don't add, next cycle we add 1, next one we add 10, ...)

So instead of building out the array, we do these calculations:

(n - 1) // (cycle length)
(n - 1) % (cycle length)

For this example:
13 // 4 = 3
13 % 4 = 1

3 in binary = 11
1 in binary = 1

This tells us we need to fill in the 0s in x with 1 (from right to left),
and add '11' to the left of the result, and that is the answer.

Which would look like this:

 1 0 0  <- x
     1  <- 13 % 4 in binary
 -----
 1 0 1

Add '11' to the left:

1 1 1 0 1

which is 29.
'''

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        zero_count = bin(x)[2:].count('0')
        cycle_length = 1 << zero_count
        num_cycles = (n-1) // cycle_length
        remainder = (n-1) % cycle_length
        ans = deque()

        bin_x = bin(x)[2:]

        # For remainder, fill in the 0s with binary version of remainder
        if remainder >= 1:
            bin_rem = bin(remainder)[2:]
            r = len(bin_rem) - 1  # index of bin_remainder

            for i in range(len(bin_x) - 1, -1, -1):
                if bin_x[i] == '0':
                    if r >= 0:
                        # Fill in with bin_rem value
                        ans.appendleft(bin_rem[r])
                        r -= 1
                    else:
                        ans.appendleft('0')
                else:
                    ans.appendleft('1')
        else:
            ans.append(bin_x)

        # For cycles, add binary equivalent of cycles to the left
        if cycle_length >= 1:
            bin_cycles = bin(num_cycles)[2:]
            ans.appendleft(bin_cycles)

        return int(''.join(ans), 2)
        

'''
Test cases:
n = 6, x = 4
=> 13

n = 7, x = 17
=> 29

n = 5, x = 17
=> 25

n = 3, x = 17
=> 21

n = 9, x = 17
=> 49
'''
