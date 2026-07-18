"""
Solution derived by looking at a simple pattern.
Input:
n = 6, s = 3, m = 5

3 8 7 12 11 16 
3 8 | 7 12 | 11 16 

(-1 then +4 to derive each group which gives maximized values)
each group of two increases by 4 ( = m - 1) from the last group.
So with the index, we can get which group its in, and whether its
the first or second number in that group, and calculate the answer.
The formula is 
    s + group * (m-1) + 1
because between each group, it increases by (m-1)
'group' finds out which group it is in.
For the first numbers in each group, we just consider it to be in the last group
which is why I did "(n - 1) // 2" to calculate the group ( - 1 gets the last group)
The +1 is because the first group increments the starting number, s, by m
and then ever other group increments it by (m-1)

TC = O(1)
SC = O(1)
"""
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
            
        elif n % 2 == 0:
            group = n // 2
            return s + group * (m-1) + 1

        else:
            group = (n - 1) // 2
            return s + group * (m-1) + 1
