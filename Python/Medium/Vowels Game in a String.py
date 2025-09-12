"""
After analyzing all cases, the only time Alice loses is when there are no
vowels, since she must take at least one but cannot. With at least one vowel,
Alice can always win: if the vowels are odd, she takes them all; if even, she
can still force a win by leaving Bob with an unfavorable choice. The solution is
to check if the string has at least one vowel.
Time complexity: O(N)
space complexity: O(1)
"""

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        return any(c in vowels for c in s)

"""  
0 vowels:
wxyz
xyz
x
- Alice always loses because she can never take any, since she needs to take
  at least 1 vowel

Even num vowels:
2 vowels:
oo
- alice takes 1, bob can't take, alice wins

xoox
- alice takes 1 (xo), bob takes x, alice takes 1, alice wins

xoo
- alice can take (xo) to win

oox
- alice can take (ox) to win

oxxxo
- alice can take (oxxx) or (xxxo) to win

4 vowels:
oooo

ollloolllo

lloolloo

oollooll

- alice can win in all of them


Odd num vowels:
leetcooder
- Alice can always win by taking the whole string

Looks like Alice can win in every case except when there are no vowels
"""
