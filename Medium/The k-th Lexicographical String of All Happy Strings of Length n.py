"""
See my solution post:
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/solutions/6440549/on-solution-beats-100-division-by-david1-b8vf/
"""

"""  
I solved this problem by just listing out each string in order for 
n = 1, 2, 3, 4, and partialy 5.
I saw a pattern:

List of strings of length 1:
a
b
c

List of 6 strings of length 2:
ab
ac
ba
bc
ca
cb

List of 12 strings of length 3:
aba
abc
aca
acb
bab
bac
bca
bcb
cab
cac
cba
cbc

List of 18 strings of length 4:
abab
abac
abca
abcb
acab
acac
acba
acbc
baba
babc
baca
bacb
bcab
bcac
bcba
bcbc
caba
cabc
caca
cacb
cbab
cbac
cbca
cbcb

List of 24 strings of length 5:
ababa
ababc
abaca
abacb
abcab
abcac
abcba
abcbc
acaba
acabc
acaca
acacb
acbab
acbac
acbca
acbcb
babab
...

There are 3 * 2^(n-1) strings.
I derived that because n = 1 has 3 strings, and each one after that doubles in size.
I noticed that each one is divided into 3 groups of equal size, each starting with the letters
a, b, c, respectively. 
Then, each group is divided intwo two groups, where the first group has the next lexicographical letter,
and the second group has the next lexicograpihcal letter after that. And those groups divide into 2,
and this repeats until the last letter.
So this pattern led to the solution below.
One of the hardest I've solved I think. 
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total_strings = 3 * 2 ** (n - 1)
        
        if k > total_strings:
            return ''

        # First third starts with a, second with b, third with c
        # So I divide by 3 to find out
        one_third = total_strings // 3

        # Subtract by 1 because if n == 4 for example, 
        # 1-8 start with a,
        # but although 1/8 == 0 and 7/8 == 0, 8/8 == 1
        # so this subtracting makes 8/8 == 0
        section = (k - 1) // one_third

        # Use result of division to find out first letter
        ans = []
        match section:
            case 0:
                ans.append('a')
            case 1:
                ans.append('b')
            case 2:
                ans.append('c')

        # We then calculate the next letters
        # 'section' will now be 0 or 1, which
        # tell us which letter came next
        # because in each section from above, half of the strings
        # in each section start with one letter (lexicograpihically smallest)
        # and the second half starts with the next letter possible
        # and this repeats recursively for each next letter
        k -= section * one_third

        one_half = one_third // 2

        while one_half:
            section = (k - 1) // one_half

            match section:
                case 0:
                    ans.append(self.next_letter(ans[-1], 1))
                case 1:
                    ans.append(self.next_letter(ans[-1], 2))
                    k -= one_half

            one_half >>= 1

        return ''.join(ans)

    """  
    'letter' is the previous letter we are getting the next letter for
    'distance' says whether we want the next lexicograpihcally smallest
    letter or the 2nd next one.
    """
    def next_letter(self, letter, distance):
            match letter:
                case 'a':
                    match distance:
                        case 1:
                            return 'b'
                        case 2:
                            return 'c'
                case 'b':
                    match distance:
                        case 1:
                            return 'a'
                        case 2:
                            return 'c'
                case 'c':
                    match distance:
                        case 1:
                            return 'a'
                        case 2:
                            return 'b'
                
