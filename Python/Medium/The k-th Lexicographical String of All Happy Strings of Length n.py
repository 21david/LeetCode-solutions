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

List of 24 strings of length 4:
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

List of 48 strings of length 5:
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

TC: O(N)
SC: O(N)
Beats 100% of other solutions in time taken.
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
                



"""
Solution 2: Backtracking
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = [None] * n
        found = 0
        final_ans = None

        def find(i):
            nonlocal found, final_ans
            if final_ans:
                return

            if i == n:
                found += 1
                if found == k:
                    final_ans = ''.join(ans)
                return 

            for letter in ('a', 'b', 'c'):
                if i == 0 or letter != ans[i - 1]:
                    ans[i] = letter
                    find(i + 1)

        find(0)
        return final_ans or ''


# print(''.join(ans), found, 'yes' if found == k else '')  # line 15


"""
Solution 3: Precomputed results
See my solution post:
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/solutions/6443642/o1-solution-by-precomputing-all-possible-yvyu/

I used the O(N) algorithm to calculate the results and just return it
based on the input.

TC: O(1)
SC: O(1)
"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        match n: 
            case 1: 
                ans = [None, 'a', 'b', 'c']
            case 2: 
                ans = [None, 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
            case 3: 
                ans = [None, 'aba', 'abc', 'aca', 'acb', 'bab', 'bac', 'bca', 'bcb', 'cab', 'cac', 'cba', 'cbc']
            case 4: 
                ans = [None, 'abab', 'abac', 'abca', 'abcb', 'acab', 'acac', 'acba', 'acbc', 'baba', 'babc', 'baca', 'bacb', 'bcab', 'bcac', 'bcba', 'bcbc', 'caba', 'cabc', 'caca', 'cacb', 
                        'cbab', 'cbac', 'cbca', 'cbcb']
            case 5: 
                ans = [None, 'ababa', 'ababc', 'abaca', 'abacb', 'abcab', 'abcac', 'abcba', 'abcbc', 'acaba', 'acabc', 'acaca', 'acacb', 'acbab', 'acbac', 'acbca', 'acbcb', 'babab', 'babac', 'babca', 'babcb', 
                        'bacab', 'bacac', 'bacba', 'bacbc', 'bcaba', 'bcabc', 'bcaca', 'bcacb', 'bcbab', 'bcbac', 'bcbca', 'bcbcb', 'cabab', 'cabac', 'cabca', 'cabcb', 'cacab', 'cacac', 'cacba', 'cacbc', 
                        'cbaba', 'cbabc', 'cbaca', 'cbacb', 'cbcab', 'cbcac', 'cbcba', 'cbcbc']
            case 6: 
                ans = [None, 'ababab', 'ababac', 'ababca', 'ababcb', 'abacab', 'abacac', 'abacba', 'abacbc', 'abcaba', 'abcabc', 'abcaca', 'abcacb', 'abcbab', 'abcbac', 'abcbca', 'abcbcb', 'acabab', 'acabac', 'acabca', 'acabcb', 
                        'acacab', 'acacac', 'acacba', 'acacbc', 'acbaba', 'acbabc', 'acbaca', 'acbacb', 'acbcab', 'acbcac', 'acbcba', 'acbcbc', 'bababa', 'bababc', 'babaca', 'babacb', 'babcab', 'babcac', 'babcba', 'babcbc', 
                        'bacaba', 'bacabc', 'bacaca', 'bacacb', 'bacbab', 'bacbac', 'bacbca', 'bacbcb', 'bcabab', 'bcabac', 'bcabca', 'bcabcb', 'bcacab', 'bcacac', 'bcacba', 'bcacbc', 'bcbaba', 'bcbabc', 'bcbaca', 'bcbacb', 
                        'bcbcab', 'bcbcac', 'bcbcba', 'bcbcbc', 'cababa', 'cababc', 'cabaca', 'cabacb', 'cabcab', 'cabcac', 'cabcba', 'cabcbc', 'cacaba', 'cacabc', 'cacaca', 'cacacb', 'cacbab', 'cacbac', 'cacbca', 'cacbcb', 
                        'cbabab', 'cbabac', 'cbabca', 'cbabcb', 'cbacab', 'cbacac', 'cbacba', 'cbacbc', 'cbcaba', 'cbcabc', 'cbcaca', 'cbcacb', 'cbcbab', 'cbcbac', 'cbcbca', 'cbcbcb']
            case 7: 
                ans = [None, 'abababa', 'abababc', 'ababaca', 'ababacb', 'ababcab', 'ababcac', 'ababcba', 'ababcbc', 'abacaba', 'abacabc', 'abacaca', 'abacacb', 'abacbab', 'abacbac', 'abacbca', 'abacbcb', 'abcabab', 'abcabac', 'abcabca', 'abcabcb', 
                        'abcacab', 'abcacac', 'abcacba', 'abcacbc', 'abcbaba', 'abcbabc', 'abcbaca', 'abcbacb', 'abcbcab', 'abcbcac', 'abcbcba', 'abcbcbc', 'acababa', 'acababc', 'acabaca', 'acabacb', 'acabcab', 'acabcac', 'acabcba', 'acabcbc', 
                        'acacaba', 'acacabc', 'acacaca', 'acacacb', 'acacbab', 'acacbac', 'acacbca', 'acacbcb', 'acbabab', 'acbabac', 'acbabca', 'acbabcb', 'acbacab', 'acbacac', 'acbacba', 'acbacbc', 'acbcaba', 'acbcabc', 'acbcaca', 'acbcacb', 
                        'acbcbab', 'acbcbac', 'acbcbca', 'acbcbcb', 'bababab', 'bababac', 'bababca', 'bababcb', 'babacab', 'babacac', 'babacba', 'babacbc', 'babcaba', 'babcabc', 'babcaca', 'babcacb', 'babcbab', 'babcbac', 'babcbca', 'babcbcb', 
                        'bacabab', 'bacabac', 'bacabca', 'bacabcb', 'bacacab', 'bacacac', 'bacacba', 'bacacbc', 'bacbaba', 'bacbabc', 'bacbaca', 'bacbacb', 'bacbcab', 'bacbcac', 'bacbcba', 'bacbcbc', 'bcababa', 'bcababc', 'bcabaca', 'bcabacb', 
                        'bcabcab', 'bcabcac', 'bcabcba', 'bcabcbc', 'bcacaba', 'bcacabc', 'bcacaca', 'bcacacb', 'bcacbab', 'bcacbac', 'bcacbca', 'bcacbcb', 'bcbabab', 'bcbabac', 'bcbabca', 'bcbabcb', 'bcbacab', 'bcbacac', 'bcbacba', 'bcbacbc', 
                        'bcbcaba', 'bcbcabc', 'bcbcaca', 'bcbcacb', 'bcbcbab', 'bcbcbac', 'bcbcbca', 'bcbcbcb', 'cababab', 'cababac', 'cababca', 'cababcb', 'cabacab', 'cabacac', 'cabacba', 'cabacbc', 'cabcaba', 'cabcabc', 'cabcaca', 'cabcacb', 
                        'cabcbab', 'cabcbac', 'cabcbca', 'cabcbcb', 'cacabab', 'cacabac', 'cacabca', 'cacabcb', 'cacacab', 'cacacac', 'cacacba', 'cacacbc', 'cacbaba', 'cacbabc', 'cacbaca', 'cacbacb', 'cacbcab', 'cacbcac', 'cacbcba', 'cacbcbc', 
                        'cbababa', 'cbababc', 'cbabaca', 'cbabacb', 'cbabcab', 'cbabcac', 'cbabcba', 'cbabcbc', 'cbacaba', 'cbacabc', 'cbacaca', 'cbacacb', 'cbacbab', 'cbacbac', 'cbacbca', 'cbacbcb', 'cbcabab', 'cbcabac', 'cbcabca', 'cbcabcb', 
                        'cbcacab', 'cbcacac', 'cbcacba', 'cbcacbc', 'cbcbaba', 'cbcbabc', 'cbcbaca', 'cbcbacb', 'cbcbcab', 'cbcbcac', 'cbcbcba', 'cbcbcbc']
            case 8: 
                ans = [None, 'abababab', 'abababac', 'abababca', 'abababcb', 'ababacab', 'ababacac', 'ababacba', 'ababacbc', 'ababcaba', 'ababcabc', 'ababcaca', 'ababcacb', 'ababcbab', 'ababcbac', 'ababcbca', 'ababcbcb', 'abacabab', 'abacabac', 'abacabca', 'abacabcb', 
                        'abacacab', 'abacacac', 'abacacba', 'abacacbc', 'abacbaba', 'abacbabc', 'abacbaca', 'abacbacb', 'abacbcab', 'abacbcac', 'abacbcba', 'abacbcbc', 'abcababa', 'abcababc', 'abcabaca', 'abcabacb', 'abcabcab', 'abcabcac', 'abcabcba', 'abcabcbc', 
                        'abcacaba', 'abcacabc', 'abcacaca', 'abcacacb', 'abcacbab', 'abcacbac', 'abcacbca', 'abcacbcb', 'abcbabab', 'abcbabac', 'abcbabca', 'abcbabcb', 'abcbacab', 'abcbacac', 'abcbacba', 'abcbacbc', 'abcbcaba', 'abcbcabc', 'abcbcaca', 'abcbcacb', 
                        'abcbcbab', 'abcbcbac', 'abcbcbca', 'abcbcbcb', 'acababab', 'acababac', 'acababca', 'acababcb', 'acabacab', 'acabacac', 'acabacba', 'acabacbc', 'acabcaba', 'acabcabc', 'acabcaca', 'acabcacb', 'acabcbab', 'acabcbac', 'acabcbca', 'acabcbcb', 
                        'acacabab', 'acacabac', 'acacabca', 'acacabcb', 'acacacab', 'acacacac', 'acacacba', 'acacacbc', 'acacbaba', 'acacbabc', 'acacbaca', 'acacbacb', 'acacbcab', 'acacbcac', 'acacbcba', 'acacbcbc', 'acbababa', 'acbababc', 'acbabaca', 'acbabacb', 
                        'acbabcab', 'acbabcac', 'acbabcba', 'acbabcbc', 'acbacaba', 'acbacabc', 'acbacaca', 'acbacacb', 'acbacbab', 'acbacbac', 'acbacbca', 'acbacbcb', 'acbcabab', 'acbcabac', 'acbcabca', 'acbcabcb', 'acbcacab', 'acbcacac', 'acbcacba', 'acbcacbc', 
                        'acbcbaba', 'acbcbabc', 'acbcbaca', 'acbcbacb', 'acbcbcab', 'acbcbcac', 'acbcbcba', 'acbcbcbc', 'babababa', 'babababc', 'bababaca', 'bababacb', 'bababcab', 'bababcac', 'bababcba', 'bababcbc', 'babacaba', 'babacabc', 'babacaca', 'babacacb', 
                        'babacbab', 'babacbac', 'babacbca', 'babacbcb', 'babcabab', 'babcabac', 'babcabca', 'babcabcb', 'babcacab', 'babcacac', 'babcacba', 'babcacbc', 'babcbaba', 'babcbabc', 'babcbaca', 'babcbacb', 'babcbcab', 'babcbcac', 'babcbcba', 'babcbcbc', 
                        'bacababa', 'bacababc', 'bacabaca', 'bacabacb', 'bacabcab', 'bacabcac', 'bacabcba', 'bacabcbc', 'bacacaba', 'bacacabc', 'bacacaca', 'bacacacb', 'bacacbab', 'bacacbac', 'bacacbca', 'bacacbcb', 'bacbabab', 'bacbabac', 'bacbabca', 'bacbabcb', 
                        'bacbacab', 'bacbacac', 'bacbacba', 'bacbacbc', 'bacbcaba', 'bacbcabc', 'bacbcaca', 'bacbcacb', 'bacbcbab', 'bacbcbac', 'bacbcbca', 'bacbcbcb', 'bcababab', 'bcababac', 'bcababca', 'bcababcb', 'bcabacab', 'bcabacac', 'bcabacba', 'bcabacbc', 
                        'bcabcaba', 'bcabcabc', 'bcabcaca', 'bcabcacb', 'bcabcbab', 'bcabcbac', 'bcabcbca', 'bcabcbcb', 'bcacabab', 'bcacabac', 'bcacabca', 'bcacabcb', 'bcacacab', 'bcacacac', 'bcacacba', 'bcacacbc', 'bcacbaba', 'bcacbabc', 'bcacbaca', 'bcacbacb', 
                        'bcacbcab', 'bcacbcac', 'bcacbcba', 'bcacbcbc', 'bcbababa', 'bcbababc', 'bcbabaca', 'bcbabacb', 'bcbabcab', 'bcbabcac', 'bcbabcba', 'bcbabcbc', 'bcbacaba', 'bcbacabc', 'bcbacaca', 'bcbacacb', 'bcbacbab', 'bcbacbac', 'bcbacbca', 'bcbacbcb', 
                        'bcbcabab', 'bcbcabac', 'bcbcabca', 'bcbcabcb', 'bcbcacab', 'bcbcacac', 'bcbcacba', 'bcbcacbc', 'bcbcbaba', 'bcbcbabc', 'bcbcbaca', 'bcbcbacb', 'bcbcbcab', 'bcbcbcac', 'bcbcbcba', 'bcbcbcbc', 'cabababa', 'cabababc', 'cababaca', 'cababacb', 
                        'cababcab', 'cababcac', 'cababcba', 'cababcbc', 'cabacaba', 'cabacabc', 'cabacaca', 'cabacacb', 'cabacbab', 'cabacbac', 'cabacbca', 'cabacbcb', 'cabcabab', 'cabcabac', 'cabcabca', 'cabcabcb', 'cabcacab', 'cabcacac', 'cabcacba', 'cabcacbc', 
                        'cabcbaba', 'cabcbabc', 'cabcbaca', 'cabcbacb', 'cabcbcab', 'cabcbcac', 'cabcbcba', 'cabcbcbc', 'cacababa', 'cacababc', 'cacabaca', 'cacabacb', 'cacabcab', 'cacabcac', 'cacabcba', 'cacabcbc', 'cacacaba', 'cacacabc', 'cacacaca', 'cacacacb', 
                        'cacacbab', 'cacacbac', 'cacacbca', 'cacacbcb', 'cacbabab', 'cacbabac', 'cacbabca', 'cacbabcb', 'cacbacab', 'cacbacac', 'cacbacba', 'cacbacbc', 'cacbcaba', 'cacbcabc', 'cacbcaca', 'cacbcacb', 'cacbcbab', 'cacbcbac', 'cacbcbca', 'cacbcbcb', 
                        'cbababab', 'cbababac', 'cbababca', 'cbababcb', 'cbabacab', 'cbabacac', 'cbabacba', 'cbabacbc', 'cbabcaba', 'cbabcabc', 'cbabcaca', 'cbabcacb', 'cbabcbab', 'cbabcbac', 'cbabcbca', 'cbabcbcb', 'cbacabab', 'cbacabac', 'cbacabca', 'cbacabcb', 
                        'cbacacab', 'cbacacac', 'cbacacba', 'cbacacbc', 'cbacbaba', 'cbacbabc', 'cbacbaca', 'cbacbacb', 'cbacbcab', 'cbacbcac', 'cbacbcba', 'cbacbcbc', 'cbcababa', 'cbcababc', 'cbcabaca', 'cbcabacb', 'cbcabcab', 'cbcabcac', 'cbcabcba', 'cbcabcbc', 
                        'cbcacaba', 'cbcacabc', 'cbcacaca', 'cbcacacb', 'cbcacbab', 'cbcacbac', 'cbcacbca', 'cbcacbcb', 'cbcbabab', 'cbcbabac', 'cbcbabca', 'cbcbabcb', 'cbcbacab', 'cbcbacac', 'cbcbacba', 'cbcbacbc', 'cbcbcaba', 'cbcbcabc', 'cbcbcaca', 'cbcbcacb', 
                        'cbcbcbab', 'cbcbcbac', 'cbcbcbca', 'cbcbcbcb']
            case 9: 
                ans = [None, 'ababababa', 'ababababc', 'abababaca', 'abababacb', 'abababcab', 'abababcac', 'abababcba', 'abababcbc', 'ababacaba', 'ababacabc', 'ababacaca', 'ababacacb', 'ababacbab', 'ababacbac', 'ababacbca', 'ababacbcb', 'ababcabab', 'ababcabac', 'ababcabca', 'ababcabcb', 
                        'ababcacab', 'ababcacac', 'ababcacba', 'ababcacbc', 'ababcbaba', 'ababcbabc', 'ababcbaca', 'ababcbacb', 'ababcbcab', 'ababcbcac', 'ababcbcba', 'ababcbcbc', 'abacababa', 'abacababc', 'abacabaca', 'abacabacb', 'abacabcab', 'abacabcac', 'abacabcba', 'abacabcbc', 
                        'abacacaba', 'abacacabc', 'abacacaca', 'abacacacb', 'abacacbab', 'abacacbac', 'abacacbca', 'abacacbcb', 'abacbabab', 'abacbabac', 'abacbabca', 'abacbabcb', 'abacbacab', 'abacbacac', 'abacbacba', 'abacbacbc', 'abacbcaba', 'abacbcabc', 'abacbcaca', 'abacbcacb', 
                        'abacbcbab', 'abacbcbac', 'abacbcbca', 'abacbcbcb', 'abcababab', 'abcababac', 'abcababca', 'abcababcb', 'abcabacab', 'abcabacac', 'abcabacba', 'abcabacbc', 'abcabcaba', 'abcabcabc', 'abcabcaca', 'abcabcacb', 'abcabcbab', 'abcabcbac', 'abcabcbca', 'abcabcbcb', 
                        'abcacabab', 'abcacabac', 'abcacabca', 'abcacabcb', 'abcacacab', 'abcacacac', 'abcacacba', 'abcacacbc', 'abcacbaba', 'abcacbabc', 'abcacbaca', 'abcacbacb', 'abcacbcab', 'abcacbcac', 'abcacbcba', 'abcacbcbc', 'abcbababa', 'abcbababc', 'abcbabaca', 'abcbabacb', 
                        'abcbabcab', 'abcbabcac', 'abcbabcba', 'abcbabcbc', 'abcbacaba', 'abcbacabc', 'abcbacaca', 'abcbacacb', 'abcbacbab', 'abcbacbac', 'abcbacbca', 'abcbacbcb', 'abcbcabab', 'abcbcabac', 'abcbcabca', 'abcbcabcb', 'abcbcacab', 'abcbcacac', 'abcbcacba', 'abcbcacbc', 
                        'abcbcbaba', 'abcbcbabc', 'abcbcbaca', 'abcbcbacb', 'abcbcbcab', 'abcbcbcac', 'abcbcbcba', 'abcbcbcbc', 'acabababa', 'acabababc', 'acababaca', 'acababacb', 'acababcab', 'acababcac', 'acababcba', 'acababcbc', 'acabacaba', 'acabacabc', 'acabacaca', 'acabacacb', 
                        'acabacbab', 'acabacbac', 'acabacbca', 'acabacbcb', 'acabcabab', 'acabcabac', 'acabcabca', 'acabcabcb', 'acabcacab', 'acabcacac', 'acabcacba', 'acabcacbc', 'acabcbaba', 'acabcbabc', 'acabcbaca', 'acabcbacb', 'acabcbcab', 'acabcbcac', 'acabcbcba', 'acabcbcbc', 
                        'acacababa', 'acacababc', 'acacabaca', 'acacabacb', 'acacabcab', 'acacabcac', 'acacabcba', 'acacabcbc', 'acacacaba', 'acacacabc', 'acacacaca', 'acacacacb', 'acacacbab', 'acacacbac', 'acacacbca', 'acacacbcb', 'acacbabab', 'acacbabac', 'acacbabca', 'acacbabcb', 
                        'acacbacab', 'acacbacac', 'acacbacba', 'acacbacbc', 'acacbcaba', 'acacbcabc', 'acacbcaca', 'acacbcacb', 'acacbcbab', 'acacbcbac', 'acacbcbca', 'acacbcbcb', 'acbababab', 'acbababac', 'acbababca', 'acbababcb', 'acbabacab', 'acbabacac', 'acbabacba', 'acbabacbc', 
                        'acbabcaba', 'acbabcabc', 'acbabcaca', 'acbabcacb', 'acbabcbab', 'acbabcbac', 'acbabcbca', 'acbabcbcb', 'acbacabab', 'acbacabac', 'acbacabca', 'acbacabcb', 'acbacacab', 'acbacacac', 'acbacacba', 'acbacacbc', 'acbacbaba', 'acbacbabc', 'acbacbaca', 'acbacbacb', 
                        'acbacbcab', 'acbacbcac', 'acbacbcba', 'acbacbcbc', 'acbcababa', 'acbcababc', 'acbcabaca', 'acbcabacb', 'acbcabcab', 'acbcabcac', 'acbcabcba', 'acbcabcbc', 'acbcacaba', 'acbcacabc', 'acbcacaca', 'acbcacacb', 'acbcacbab', 'acbcacbac', 'acbcacbca', 'acbcacbcb', 
                        'acbcbabab', 'acbcbabac', 'acbcbabca', 'acbcbabcb', 'acbcbacab', 'acbcbacac', 'acbcbacba', 'acbcbacbc', 'acbcbcaba', 'acbcbcabc', 'acbcbcaca', 'acbcbcacb', 'acbcbcbab', 'acbcbcbac', 'acbcbcbca', 'acbcbcbcb', 'babababab', 'babababac', 'babababca', 'babababcb', 
                        'bababacab', 'bababacac', 'bababacba', 'bababacbc', 'bababcaba', 'bababcabc', 'bababcaca', 'bababcacb', 'bababcbab', 'bababcbac', 'bababcbca', 'bababcbcb', 'babacabab', 'babacabac', 'babacabca', 'babacabcb', 'babacacab', 'babacacac', 'babacacba', 'babacacbc', 
                        'babacbaba', 'babacbabc', 'babacbaca', 'babacbacb', 'babacbcab', 'babacbcac', 'babacbcba', 'babacbcbc', 'babcababa', 'babcababc', 'babcabaca', 'babcabacb', 'babcabcab', 'babcabcac', 'babcabcba', 'babcabcbc', 'babcacaba', 'babcacabc', 'babcacaca', 'babcacacb', 
                        'babcacbab', 'babcacbac', 'babcacbca', 'babcacbcb', 'babcbabab', 'babcbabac', 'babcbabca', 'babcbabcb', 'babcbacab', 'babcbacac', 'babcbacba', 'babcbacbc', 'babcbcaba', 'babcbcabc', 'babcbcaca', 'babcbcacb', 'babcbcbab', 'babcbcbac', 'babcbcbca', 'babcbcbcb', 
                        'bacababab', 'bacababac', 'bacababca', 'bacababcb', 'bacabacab', 'bacabacac', 'bacabacba', 'bacabacbc', 'bacabcaba', 'bacabcabc', 'bacabcaca', 'bacabcacb', 'bacabcbab', 'bacabcbac', 'bacabcbca', 'bacabcbcb', 'bacacabab', 'bacacabac', 'bacacabca', 'bacacabcb', 
                        'bacacacab', 'bacacacac', 'bacacacba', 'bacacacbc', 'bacacbaba', 'bacacbabc', 'bacacbaca', 'bacacbacb', 'bacacbcab', 'bacacbcac', 'bacacbcba', 'bacacbcbc', 'bacbababa', 'bacbababc', 'bacbabaca', 'bacbabacb', 'bacbabcab', 'bacbabcac', 'bacbabcba', 'bacbabcbc', 
                        'bacbacaba', 'bacbacabc', 'bacbacaca', 'bacbacacb', 'bacbacbab', 'bacbacbac', 'bacbacbca', 'bacbacbcb', 'bacbcabab', 'bacbcabac', 'bacbcabca', 'bacbcabcb', 'bacbcacab', 'bacbcacac', 'bacbcacba', 'bacbcacbc', 'bacbcbaba', 'bacbcbabc', 'bacbcbaca', 'bacbcbacb', 
                        'bacbcbcab', 'bacbcbcac', 'bacbcbcba', 'bacbcbcbc', 'bcabababa', 'bcabababc', 'bcababaca', 'bcababacb', 'bcababcab', 'bcababcac', 'bcababcba', 'bcababcbc', 'bcabacaba', 'bcabacabc', 'bcabacaca', 'bcabacacb', 'bcabacbab', 'bcabacbac', 'bcabacbca', 'bcabacbcb', 
                        'bcabcabab', 'bcabcabac', 'bcabcabca', 'bcabcabcb', 'bcabcacab', 'bcabcacac', 'bcabcacba', 'bcabcacbc', 'bcabcbaba', 'bcabcbabc', 'bcabcbaca', 'bcabcbacb', 'bcabcbcab', 'bcabcbcac', 'bcabcbcba', 'bcabcbcbc', 'bcacababa', 'bcacababc', 'bcacabaca', 'bcacabacb', 
                        'bcacabcab', 'bcacabcac', 'bcacabcba', 'bcacabcbc', 'bcacacaba', 'bcacacabc', 'bcacacaca', 'bcacacacb', 'bcacacbab', 'bcacacbac', 'bcacacbca', 'bcacacbcb', 'bcacbabab', 'bcacbabac', 'bcacbabca', 'bcacbabcb', 'bcacbacab', 'bcacbacac', 'bcacbacba', 'bcacbacbc', 
                        'bcacbcaba', 'bcacbcabc', 'bcacbcaca', 'bcacbcacb', 'bcacbcbab', 'bcacbcbac', 'bcacbcbca', 'bcacbcbcb', 'bcbababab', 'bcbababac', 'bcbababca', 'bcbababcb', 'bcbabacab', 'bcbabacac', 'bcbabacba', 'bcbabacbc', 'bcbabcaba', 'bcbabcabc', 'bcbabcaca', 'bcbabcacb', 
                        'bcbabcbab', 'bcbabcbac', 'bcbabcbca', 'bcbabcbcb', 'bcbacabab', 'bcbacabac', 'bcbacabca', 'bcbacabcb', 'bcbacacab', 'bcbacacac', 'bcbacacba', 'bcbacacbc', 'bcbacbaba', 'bcbacbabc', 'bcbacbaca', 'bcbacbacb', 'bcbacbcab', 'bcbacbcac', 'bcbacbcba', 'bcbacbcbc', 
                        'bcbcababa', 'bcbcababc', 'bcbcabaca', 'bcbcabacb', 'bcbcabcab', 'bcbcabcac', 'bcbcabcba', 'bcbcabcbc', 'bcbcacaba', 'bcbcacabc', 'bcbcacaca', 'bcbcacacb', 'bcbcacbab', 'bcbcacbac', 'bcbcacbca', 'bcbcacbcb', 'bcbcbabab', 'bcbcbabac', 'bcbcbabca', 'bcbcbabcb', 
                        'bcbcbacab', 'bcbcbacac', 'bcbcbacba', 'bcbcbacbc', 'bcbcbcaba', 'bcbcbcabc', 'bcbcbcaca', 'bcbcbcacb', 'bcbcbcbab', 'bcbcbcbac', 'bcbcbcbca', 'bcbcbcbcb', 'cabababab', 'cabababac', 'cabababca', 'cabababcb', 'cababacab', 'cababacac', 'cababacba', 'cababacbc', 
                        'cababcaba', 'cababcabc', 'cababcaca', 'cababcacb', 'cababcbab', 'cababcbac', 'cababcbca', 'cababcbcb', 'cabacabab', 'cabacabac', 'cabacabca', 'cabacabcb', 'cabacacab', 'cabacacac', 'cabacacba', 'cabacacbc', 'cabacbaba', 'cabacbabc', 'cabacbaca', 'cabacbacb', 
                        'cabacbcab', 'cabacbcac', 'cabacbcba', 'cabacbcbc', 'cabcababa', 'cabcababc', 'cabcabaca', 'cabcabacb', 'cabcabcab', 'cabcabcac', 'cabcabcba', 'cabcabcbc', 'cabcacaba', 'cabcacabc', 'cabcacaca', 'cabcacacb', 'cabcacbab', 'cabcacbac', 'cabcacbca', 'cabcacbcb', 
                        'cabcbabab', 'cabcbabac', 'cabcbabca', 'cabcbabcb', 'cabcbacab', 'cabcbacac', 'cabcbacba', 'cabcbacbc', 'cabcbcaba', 'cabcbcabc', 'cabcbcaca', 'cabcbcacb', 'cabcbcbab', 'cabcbcbac', 'cabcbcbca', 'cabcbcbcb', 'cacababab', 'cacababac', 'cacababca', 'cacababcb', 
                        'cacabacab', 'cacabacac', 'cacabacba', 'cacabacbc', 'cacabcaba', 'cacabcabc', 'cacabcaca', 'cacabcacb', 'cacabcbab', 'cacabcbac', 'cacabcbca', 'cacabcbcb', 'cacacabab', 'cacacabac', 'cacacabca', 'cacacabcb', 'cacacacab', 'cacacacac', 'cacacacba', 'cacacacbc', 
                        'cacacbaba', 'cacacbabc', 'cacacbaca', 'cacacbacb', 'cacacbcab', 'cacacbcac', 'cacacbcba', 'cacacbcbc', 'cacbababa', 'cacbababc', 'cacbabaca', 'cacbabacb', 'cacbabcab', 'cacbabcac', 'cacbabcba', 'cacbabcbc', 'cacbacaba', 'cacbacabc', 'cacbacaca', 'cacbacacb', 
                        'cacbacbab', 'cacbacbac', 'cacbacbca', 'cacbacbcb', 'cacbcabab', 'cacbcabac', 'cacbcabca', 'cacbcabcb', 'cacbcacab', 'cacbcacac', 'cacbcacba', 'cacbcacbc', 'cacbcbaba', 'cacbcbabc', 'cacbcbaca', 'cacbcbacb', 'cacbcbcab', 'cacbcbcac', 'cacbcbcba', 'cacbcbcbc', 
                        'cbabababa', 'cbabababc', 'cbababaca', 'cbababacb', 'cbababcab', 'cbababcac', 'cbababcba', 'cbababcbc', 'cbabacaba', 'cbabacabc', 'cbabacaca', 'cbabacacb', 'cbabacbab', 'cbabacbac', 'cbabacbca', 'cbabacbcb', 'cbabcabab', 'cbabcabac', 'cbabcabca', 'cbabcabcb', 
                        'cbabcacab', 'cbabcacac', 'cbabcacba', 'cbabcacbc', 'cbabcbaba', 'cbabcbabc', 'cbabcbaca', 'cbabcbacb', 'cbabcbcab', 'cbabcbcac', 'cbabcbcba', 'cbabcbcbc', 'cbacababa', 'cbacababc', 'cbacabaca', 'cbacabacb', 'cbacabcab', 'cbacabcac', 'cbacabcba', 'cbacabcbc', 
                        'cbacacaba', 'cbacacabc', 'cbacacaca', 'cbacacacb', 'cbacacbab', 'cbacacbac', 'cbacacbca', 'cbacacbcb', 'cbacbabab', 'cbacbabac', 'cbacbabca', 'cbacbabcb', 'cbacbacab', 'cbacbacac', 'cbacbacba', 'cbacbacbc', 'cbacbcaba', 'cbacbcabc', 'cbacbcaca', 'cbacbcacb', 
                        'cbacbcbab', 'cbacbcbac', 'cbacbcbca', 'cbacbcbcb', 'cbcababab', 'cbcababac', 'cbcababca', 'cbcababcb', 'cbcabacab', 'cbcabacac', 'cbcabacba', 'cbcabacbc', 'cbcabcaba', 'cbcabcabc', 'cbcabcaca', 'cbcabcacb', 'cbcabcbab', 'cbcabcbac', 'cbcabcbca', 'cbcabcbcb', 
                        'cbcacabab', 'cbcacabac', 'cbcacabca', 'cbcacabcb', 'cbcacacab', 'cbcacacac', 'cbcacacba', 'cbcacacbc', 'cbcacbaba', 'cbcacbabc', 'cbcacbaca', 'cbcacbacb', 'cbcacbcab', 'cbcacbcac', 'cbcacbcba', 'cbcacbcbc', 'cbcbababa', 'cbcbababc', 'cbcbabaca', 'cbcbabacb', 
                        'cbcbabcab', 'cbcbabcac', 'cbcbabcba', 'cbcbabcbc', 'cbcbacaba', 'cbcbacabc', 'cbcbacaca', 'cbcbacacb', 'cbcbacbab', 'cbcbacbac', 'cbcbacbca', 'cbcbacbcb', 'cbcbcabab', 'cbcbcabac', 'cbcbcabca', 'cbcbcabcb', 'cbcbcacab', 'cbcbcacac', 'cbcbcacba', 'cbcbcacbc', 
                        'cbcbcbaba', 'cbcbcbabc', 'cbcbcbaca', 'cbcbcbacb', 'cbcbcbcab', 'cbcbcbcac', 'cbcbcbcba', 'cbcbcbcbc']
            case 10: 
                ans = [None, 'ababababab', 'ababababac', 'ababababca', 'ababababcb', 'abababacab', 'abababacac', 'abababacba', 'abababacbc', 'abababcaba', 'abababcabc', 'abababcaca', 'abababcacb', 'abababcbab', 'abababcbac', 'abababcbca', 'abababcbcb', 'ababacabab', 'ababacabac', 'ababacabca', 'ababacabcb', 
                        'ababacacab', 'ababacacac', 'ababacacba', 'ababacacbc', 'ababacbaba', 'ababacbabc', 'ababacbaca', 'ababacbacb', 'ababacbcab', 'ababacbcac', 'ababacbcba', 'ababacbcbc', 'ababcababa', 'ababcababc', 'ababcabaca', 'ababcabacb', 'ababcabcab', 'ababcabcac', 'ababcabcba', 'ababcabcbc', 
                        'ababcacaba', 'ababcacabc', 'ababcacaca', 'ababcacacb', 'ababcacbab', 'ababcacbac', 'ababcacbca', 'ababcacbcb', 'ababcbabab', 'ababcbabac', 'ababcbabca', 'ababcbabcb', 'ababcbacab', 'ababcbacac', 'ababcbacba', 'ababcbacbc', 'ababcbcaba', 'ababcbcabc', 'ababcbcaca', 'ababcbcacb', 
                        'ababcbcbab', 'ababcbcbac', 'ababcbcbca', 'ababcbcbcb', 'abacababab', 'abacababac', 'abacababca', 'abacababcb', 'abacabacab', 'abacabacac', 'abacabacba', 'abacabacbc', 'abacabcaba', 'abacabcabc', 'abacabcaca', 'abacabcacb', 'abacabcbab', 'abacabcbac', 'abacabcbca', 'abacabcbcb', 
                        'abacacabab', 'abacacabac', 'abacacabca', 'abacacabcb', 'abacacacab', 'abacacacac', 'abacacacba', 'abacacacbc', 'abacacbaba', 'abacacbabc', 'abacacbaca', 'abacacbacb', 'abacacbcab', 'abacacbcac', 'abacacbcba', 'abacacbcbc', 'abacbababa', 'abacbababc', 'abacbabaca', 'abacbabacb', 
                        'abacbabcab', 'abacbabcac', 'abacbabcba', 'abacbabcbc', 'abacbacaba', 'abacbacabc', 'abacbacaca', 'abacbacacb', 'abacbacbab', 'abacbacbac', 'abacbacbca', 'abacbacbcb', 'abacbcabab', 'abacbcabac', 'abacbcabca', 'abacbcabcb', 'abacbcacab', 'abacbcacac', 'abacbcacba', 'abacbcacbc', 
                        'abacbcbaba', 'abacbcbabc', 'abacbcbaca', 'abacbcbacb', 'abacbcbcab', 'abacbcbcac', 'abacbcbcba', 'abacbcbcbc', 'abcabababa', 'abcabababc', 'abcababaca', 'abcababacb', 'abcababcab', 'abcababcac', 'abcababcba', 'abcababcbc', 'abcabacaba', 'abcabacabc', 'abcabacaca', 'abcabacacb', 
                        'abcabacbab', 'abcabacbac', 'abcabacbca', 'abcabacbcb', 'abcabcabab', 'abcabcabac', 'abcabcabca', 'abcabcabcb', 'abcabcacab', 'abcabcacac', 'abcabcacba', 'abcabcacbc', 'abcabcbaba', 'abcabcbabc', 'abcabcbaca', 'abcabcbacb', 'abcabcbcab', 'abcabcbcac', 'abcabcbcba', 'abcabcbcbc', 
                        'abcacababa', 'abcacababc', 'abcacabaca', 'abcacabacb', 'abcacabcab', 'abcacabcac', 'abcacabcba', 'abcacabcbc', 'abcacacaba', 'abcacacabc', 'abcacacaca', 'abcacacacb', 'abcacacbab', 'abcacacbac', 'abcacacbca', 'abcacacbcb', 'abcacbabab', 'abcacbabac', 'abcacbabca', 'abcacbabcb', 
                        'abcacbacab', 'abcacbacac', 'abcacbacba', 'abcacbacbc', 'abcacbcaba', 'abcacbcabc', 'abcacbcaca', 'abcacbcacb', 'abcacbcbab', 'abcacbcbac', 'abcacbcbca', 'abcacbcbcb', 'abcbababab', 'abcbababac', 'abcbababca', 'abcbababcb', 'abcbabacab', 'abcbabacac', 'abcbabacba', 'abcbabacbc', 
                        'abcbabcaba', 'abcbabcabc', 'abcbabcaca', 'abcbabcacb', 'abcbabcbab', 'abcbabcbac', 'abcbabcbca', 'abcbabcbcb', 'abcbacabab', 'abcbacabac', 'abcbacabca', 'abcbacabcb', 'abcbacacab', 'abcbacacac', 'abcbacacba', 'abcbacacbc', 'abcbacbaba', 'abcbacbabc', 'abcbacbaca', 'abcbacbacb', 
                        'abcbacbcab', 'abcbacbcac', 'abcbacbcba', 'abcbacbcbc', 'abcbcababa', 'abcbcababc', 'abcbcabaca', 'abcbcabacb', 'abcbcabcab', 'abcbcabcac', 'abcbcabcba', 'abcbcabcbc', 'abcbcacaba', 'abcbcacabc', 'abcbcacaca', 'abcbcacacb', 'abcbcacbab', 'abcbcacbac', 'abcbcacbca', 'abcbcacbcb', 
                        'abcbcbabab', 'abcbcbabac', 'abcbcbabca', 'abcbcbabcb', 'abcbcbacab', 'abcbcbacac', 'abcbcbacba', 'abcbcbacbc', 'abcbcbcaba', 'abcbcbcabc', 'abcbcbcaca', 'abcbcbcacb', 'abcbcbcbab', 'abcbcbcbac', 'abcbcbcbca', 'abcbcbcbcb', 'acabababab', 'acabababac', 'acabababca', 'acabababcb', 
                        'acababacab', 'acababacac', 'acababacba', 'acababacbc', 'acababcaba', 'acababcabc', 'acababcaca', 'acababcacb', 'acababcbab', 'acababcbac', 'acababcbca', 'acababcbcb', 'acabacabab', 'acabacabac', 'acabacabca', 'acabacabcb', 'acabacacab', 'acabacacac', 'acabacacba', 'acabacacbc', 
                        'acabacbaba', 'acabacbabc', 'acabacbaca', 'acabacbacb', 'acabacbcab', 'acabacbcac', 'acabacbcba', 'acabacbcbc', 'acabcababa', 'acabcababc', 'acabcabaca', 'acabcabacb', 'acabcabcab', 'acabcabcac', 'acabcabcba', 'acabcabcbc', 'acabcacaba', 'acabcacabc', 'acabcacaca', 'acabcacacb', 
                        'acabcacbab', 'acabcacbac', 'acabcacbca', 'acabcacbcb', 'acabcbabab', 'acabcbabac', 'acabcbabca', 'acabcbabcb', 'acabcbacab', 'acabcbacac', 'acabcbacba', 'acabcbacbc', 'acabcbcaba', 'acabcbcabc', 'acabcbcaca', 'acabcbcacb', 'acabcbcbab', 'acabcbcbac', 'acabcbcbca', 'acabcbcbcb', 
                        'acacababab', 'acacababac', 'acacababca', 'acacababcb', 'acacabacab', 'acacabacac', 'acacabacba', 'acacabacbc', 'acacabcaba', 'acacabcabc', 'acacabcaca', 'acacabcacb', 'acacabcbab', 'acacabcbac', 'acacabcbca', 'acacabcbcb', 'acacacabab', 'acacacabac', 'acacacabca', 'acacacabcb', 
                        'acacacacab', 'acacacacac', 'acacacacba', 'acacacacbc', 'acacacbaba', 'acacacbabc', 'acacacbaca', 'acacacbacb', 'acacacbcab', 'acacacbcac', 'acacacbcba', 'acacacbcbc', 'acacbababa', 'acacbababc', 'acacbabaca', 'acacbabacb', 'acacbabcab', 'acacbabcac', 'acacbabcba', 'acacbabcbc', 
                        'acacbacaba', 'acacbacabc', 'acacbacaca', 'acacbacacb', 'acacbacbab', 'acacbacbac', 'acacbacbca', 'acacbacbcb', 'acacbcabab', 'acacbcabac', 'acacbcabca', 'acacbcabcb', 'acacbcacab', 'acacbcacac', 'acacbcacba', 'acacbcacbc', 'acacbcbaba', 'acacbcbabc', 'acacbcbaca', 'acacbcbacb', 
                        'acacbcbcab', 'acacbcbcac', 'acacbcbcba', 'acacbcbcbc', 'acbabababa', 'acbabababc', 'acbababaca', 'acbababacb', 'acbababcab', 'acbababcac', 'acbababcba', 'acbababcbc', 'acbabacaba', 'acbabacabc', 'acbabacaca', 'acbabacacb', 'acbabacbab', 'acbabacbac', 'acbabacbca', 'acbabacbcb', 
                        'acbabcabab', 'acbabcabac', 'acbabcabca', 'acbabcabcb', 'acbabcacab', 'acbabcacac', 'acbabcacba', 'acbabcacbc', 'acbabcbaba', 'acbabcbabc', 'acbabcbaca', 'acbabcbacb', 'acbabcbcab', 'acbabcbcac', 'acbabcbcba', 'acbabcbcbc', 'acbacababa', 'acbacababc', 'acbacabaca', 'acbacabacb', 
                        'acbacabcab', 'acbacabcac', 'acbacabcba', 'acbacabcbc', 'acbacacaba', 'acbacacabc', 'acbacacaca', 'acbacacacb', 'acbacacbab', 'acbacacbac', 'acbacacbca', 'acbacacbcb', 'acbacbabab', 'acbacbabac', 'acbacbabca', 'acbacbabcb', 'acbacbacab', 'acbacbacac', 'acbacbacba', 'acbacbacbc', 
                        'acbacbcaba', 'acbacbcabc', 'acbacbcaca', 'acbacbcacb', 'acbacbcbab', 'acbacbcbac', 'acbacbcbca', 'acbacbcbcb', 'acbcababab', 'acbcababac', 'acbcababca', 'acbcababcb', 'acbcabacab', 'acbcabacac', 'acbcabacba', 'acbcabacbc', 'acbcabcaba', 'acbcabcabc', 'acbcabcaca', 'acbcabcacb', 
                        'acbcabcbab', 'acbcabcbac', 'acbcabcbca', 'acbcabcbcb', 'acbcacabab', 'acbcacabac', 'acbcacabca', 'acbcacabcb', 'acbcacacab', 'acbcacacac', 'acbcacacba', 'acbcacacbc', 'acbcacbaba', 'acbcacbabc', 'acbcacbaca', 'acbcacbacb', 'acbcacbcab', 'acbcacbcac', 'acbcacbcba', 'acbcacbcbc', 
                        'acbcbababa', 'acbcbababc', 'acbcbabaca', 'acbcbabacb', 'acbcbabcab', 'acbcbabcac', 'acbcbabcba', 'acbcbabcbc', 'acbcbacaba', 'acbcbacabc', 'acbcbacaca', 'acbcbacacb', 'acbcbacbab', 'acbcbacbac', 'acbcbacbca', 'acbcbacbcb', 'acbcbcabab', 'acbcbcabac', 'acbcbcabca', 'acbcbcabcb', 
                        'acbcbcacab', 'acbcbcacac', 'acbcbcacba', 'acbcbcacbc', 'acbcbcbaba', 'acbcbcbabc', 'acbcbcbaca', 'acbcbcbacb', 'acbcbcbcab', 'acbcbcbcac', 'acbcbcbcba', 'acbcbcbcbc', 'bababababa', 'bababababc', 'babababaca', 'babababacb', 'babababcab', 'babababcac', 'babababcba', 'babababcbc', 
                        'bababacaba', 'bababacabc', 'bababacaca', 'bababacacb', 'bababacbab', 'bababacbac', 'bababacbca', 'bababacbcb', 'bababcabab', 'bababcabac', 'bababcabca', 'bababcabcb', 'bababcacab', 'bababcacac', 'bababcacba', 'bababcacbc', 'bababcbaba', 'bababcbabc', 'bababcbaca', 'bababcbacb', 
                        'bababcbcab', 'bababcbcac', 'bababcbcba', 'bababcbcbc', 'babacababa', 'babacababc', 'babacabaca', 'babacabacb', 'babacabcab', 'babacabcac', 'babacabcba', 'babacabcbc', 'babacacaba', 'babacacabc', 'babacacaca', 'babacacacb', 'babacacbab', 'babacacbac', 'babacacbca', 'babacacbcb', 
                        'babacbabab', 'babacbabac', 'babacbabca', 'babacbabcb', 'babacbacab', 'babacbacac', 'babacbacba', 'babacbacbc', 'babacbcaba', 'babacbcabc', 'babacbcaca', 'babacbcacb', 'babacbcbab', 'babacbcbac', 'babacbcbca', 'babacbcbcb', 'babcababab', 'babcababac', 'babcababca', 'babcababcb', 
                        'babcabacab', 'babcabacac', 'babcabacba', 'babcabacbc', 'babcabcaba', 'babcabcabc', 'babcabcaca', 'babcabcacb', 'babcabcbab', 'babcabcbac', 'babcabcbca', 'babcabcbcb', 'babcacabab', 'babcacabac', 'babcacabca', 'babcacabcb', 'babcacacab', 'babcacacac', 'babcacacba', 'babcacacbc', 
                        'babcacbaba', 'babcacbabc', 'babcacbaca', 'babcacbacb', 'babcacbcab', 'babcacbcac', 'babcacbcba', 'babcacbcbc', 'babcbababa', 'babcbababc', 'babcbabaca', 'babcbabacb', 'babcbabcab', 'babcbabcac', 'babcbabcba', 'babcbabcbc', 'babcbacaba', 'babcbacabc', 'babcbacaca', 'babcbacacb', 
                        'babcbacbab', 'babcbacbac', 'babcbacbca', 'babcbacbcb', 'babcbcabab', 'babcbcabac', 'babcbcabca', 'babcbcabcb', 'babcbcacab', 'babcbcacac', 'babcbcacba', 'babcbcacbc', 'babcbcbaba', 'babcbcbabc', 'babcbcbaca', 'babcbcbacb', 'babcbcbcab', 'babcbcbcac', 'babcbcbcba', 'babcbcbcbc', 
                        'bacabababa', 'bacabababc', 'bacababaca', 'bacababacb', 'bacababcab', 'bacababcac', 'bacababcba', 'bacababcbc', 'bacabacaba', 'bacabacabc', 'bacabacaca', 'bacabacacb', 'bacabacbab', 'bacabacbac', 'bacabacbca', 'bacabacbcb', 'bacabcabab', 'bacabcabac', 'bacabcabca', 'bacabcabcb', 
                        'bacabcacab', 'bacabcacac', 'bacabcacba', 'bacabcacbc', 'bacabcbaba', 'bacabcbabc', 'bacabcbaca', 'bacabcbacb', 'bacabcbcab', 'bacabcbcac', 'bacabcbcba', 'bacabcbcbc', 'bacacababa', 'bacacababc', 'bacacabaca', 'bacacabacb', 'bacacabcab', 'bacacabcac', 'bacacabcba', 'bacacabcbc', 
                        'bacacacaba', 'bacacacabc', 'bacacacaca', 'bacacacacb', 'bacacacbab', 'bacacacbac', 'bacacacbca', 'bacacacbcb', 'bacacbabab', 'bacacbabac', 'bacacbabca', 'bacacbabcb', 'bacacbacab', 'bacacbacac', 'bacacbacba', 'bacacbacbc', 'bacacbcaba', 'bacacbcabc', 'bacacbcaca', 'bacacbcacb', 
                        'bacacbcbab', 'bacacbcbac', 'bacacbcbca', 'bacacbcbcb', 'bacbababab', 'bacbababac', 'bacbababca', 'bacbababcb', 'bacbabacab', 'bacbabacac', 'bacbabacba', 'bacbabacbc', 'bacbabcaba', 'bacbabcabc', 'bacbabcaca', 'bacbabcacb', 'bacbabcbab', 'bacbabcbac', 'bacbabcbca', 'bacbabcbcb', 
                        'bacbacabab', 'bacbacabac', 'bacbacabca', 'bacbacabcb', 'bacbacacab', 'bacbacacac', 'bacbacacba', 'bacbacacbc', 'bacbacbaba', 'bacbacbabc', 'bacbacbaca', 'bacbacbacb', 'bacbacbcab', 'bacbacbcac', 'bacbacbcba', 'bacbacbcbc', 'bacbcababa', 'bacbcababc', 'bacbcabaca', 'bacbcabacb', 
                        'bacbcabcab', 'bacbcabcac', 'bacbcabcba', 'bacbcabcbc', 'bacbcacaba', 'bacbcacabc', 'bacbcacaca', 'bacbcacacb', 'bacbcacbab', 'bacbcacbac', 'bacbcacbca', 'bacbcacbcb', 'bacbcbabab', 'bacbcbabac', 'bacbcbabca', 'bacbcbabcb', 'bacbcbacab', 'bacbcbacac', 'bacbcbacba', 'bacbcbacbc', 
                        'bacbcbcaba', 'bacbcbcabc', 'bacbcbcaca', 'bacbcbcacb', 'bacbcbcbab', 'bacbcbcbac', 'bacbcbcbca', 'bacbcbcbcb', 'bcabababab', 'bcabababac', 'bcabababca', 'bcabababcb', 'bcababacab', 'bcababacac', 'bcababacba', 'bcababacbc', 'bcababcaba', 'bcababcabc', 'bcababcaca', 'bcababcacb', 
                        'bcababcbab', 'bcababcbac', 'bcababcbca', 'bcababcbcb', 'bcabacabab', 'bcabacabac', 'bcabacabca', 'bcabacabcb', 'bcabacacab', 'bcabacacac', 'bcabacacba', 'bcabacacbc', 'bcabacbaba', 'bcabacbabc', 'bcabacbaca', 'bcabacbacb', 'bcabacbcab', 'bcabacbcac', 'bcabacbcba', 'bcabacbcbc', 
                        'bcabcababa', 'bcabcababc', 'bcabcabaca', 'bcabcabacb', 'bcabcabcab', 'bcabcabcac', 'bcabcabcba', 'bcabcabcbc', 'bcabcacaba', 'bcabcacabc', 'bcabcacaca', 'bcabcacacb', 'bcabcacbab', 'bcabcacbac', 'bcabcacbca', 'bcabcacbcb', 'bcabcbabab', 'bcabcbabac', 'bcabcbabca', 'bcabcbabcb', 
                        'bcabcbacab', 'bcabcbacac', 'bcabcbacba', 'bcabcbacbc', 'bcabcbcaba', 'bcabcbcabc', 'bcabcbcaca', 'bcabcbcacb', 'bcabcbcbab', 'bcabcbcbac', 'bcabcbcbca', 'bcabcbcbcb', 'bcacababab', 'bcacababac', 'bcacababca', 'bcacababcb', 'bcacabacab', 'bcacabacac', 'bcacabacba', 'bcacabacbc', 
                        'bcacabcaba', 'bcacabcabc', 'bcacabcaca', 'bcacabcacb', 'bcacabcbab', 'bcacabcbac', 'bcacabcbca', 'bcacabcbcb', 'bcacacabab', 'bcacacabac', 'bcacacabca', 'bcacacabcb', 'bcacacacab', 'bcacacacac', 'bcacacacba', 'bcacacacbc', 'bcacacbaba', 'bcacacbabc', 'bcacacbaca', 'bcacacbacb', 
                        'bcacacbcab', 'bcacacbcac', 'bcacacbcba', 'bcacacbcbc', 'bcacbababa', 'bcacbababc', 'bcacbabaca', 'bcacbabacb', 'bcacbabcab', 'bcacbabcac', 'bcacbabcba', 'bcacbabcbc', 'bcacbacaba', 'bcacbacabc', 'bcacbacaca', 'bcacbacacb', 'bcacbacbab', 'bcacbacbac', 'bcacbacbca', 'bcacbacbcb', 
                        'bcacbcabab', 'bcacbcabac', 'bcacbcabca', 'bcacbcabcb', 'bcacbcacab', 'bcacbcacac', 'bcacbcacba', 'bcacbcacbc', 'bcacbcbaba', 'bcacbcbabc', 'bcacbcbaca', 'bcacbcbacb', 'bcacbcbcab', 'bcacbcbcac', 'bcacbcbcba', 'bcacbcbcbc', 'bcbabababa', 'bcbabababc', 'bcbababaca', 'bcbababacb', 
                        'bcbababcab', 'bcbababcac', 'bcbababcba', 'bcbababcbc', 'bcbabacaba', 'bcbabacabc', 'bcbabacaca', 'bcbabacacb', 'bcbabacbab', 'bcbabacbac', 'bcbabacbca', 'bcbabacbcb', 'bcbabcabab', 'bcbabcabac', 'bcbabcabca', 'bcbabcabcb', 'bcbabcacab', 'bcbabcacac', 'bcbabcacba', 'bcbabcacbc', 
                        'bcbabcbaba', 'bcbabcbabc', 'bcbabcbaca', 'bcbabcbacb', 'bcbabcbcab', 'bcbabcbcac', 'bcbabcbcba', 'bcbabcbcbc', 'bcbacababa', 'bcbacababc', 'bcbacabaca', 'bcbacabacb', 'bcbacabcab', 'bcbacabcac', 'bcbacabcba', 'bcbacabcbc', 'bcbacacaba', 'bcbacacabc', 'bcbacacaca', 'bcbacacacb', 
                        'bcbacacbab', 'bcbacacbac', 'bcbacacbca', 'bcbacacbcb', 'bcbacbabab', 'bcbacbabac', 'bcbacbabca', 'bcbacbabcb', 'bcbacbacab', 'bcbacbacac', 'bcbacbacba', 'bcbacbacbc', 'bcbacbcaba', 'bcbacbcabc', 'bcbacbcaca', 'bcbacbcacb', 'bcbacbcbab', 'bcbacbcbac', 'bcbacbcbca', 'bcbacbcbcb', 
                        'bcbcababab', 'bcbcababac', 'bcbcababca', 'bcbcababcb', 'bcbcabacab', 'bcbcabacac', 'bcbcabacba', 'bcbcabacbc', 'bcbcabcaba', 'bcbcabcabc', 'bcbcabcaca', 'bcbcabcacb', 'bcbcabcbab', 'bcbcabcbac', 'bcbcabcbca', 'bcbcabcbcb', 'bcbcacabab', 'bcbcacabac', 'bcbcacabca', 'bcbcacabcb', 
                        'bcbcacacab', 'bcbcacacac', 'bcbcacacba', 'bcbcacacbc', 'bcbcacbaba', 'bcbcacbabc', 'bcbcacbaca', 'bcbcacbacb', 'bcbcacbcab', 'bcbcacbcac', 'bcbcacbcba', 'bcbcacbcbc', 'bcbcbababa', 'bcbcbababc', 'bcbcbabaca', 'bcbcbabacb', 'bcbcbabcab', 'bcbcbabcac', 'bcbcbabcba', 'bcbcbabcbc', 
                        'bcbcbacaba', 'bcbcbacabc', 'bcbcbacaca', 'bcbcbacacb', 'bcbcbacbab', 'bcbcbacbac', 'bcbcbacbca', 'bcbcbacbcb', 'bcbcbcabab', 'bcbcbcabac', 'bcbcbcabca', 'bcbcbcabcb', 'bcbcbcacab', 'bcbcbcacac', 'bcbcbcacba', 'bcbcbcacbc', 'bcbcbcbaba', 'bcbcbcbabc', 'bcbcbcbaca', 'bcbcbcbacb', 
                        'bcbcbcbcab', 'bcbcbcbcac', 'bcbcbcbcba', 'bcbcbcbcbc', 'cababababa', 'cababababc', 'cabababaca', 'cabababacb', 'cabababcab', 'cabababcac', 'cabababcba', 'cabababcbc', 'cababacaba', 'cababacabc', 'cababacaca', 'cababacacb', 'cababacbab', 'cababacbac', 'cababacbca', 'cababacbcb', 
                        'cababcabab', 'cababcabac', 'cababcabca', 'cababcabcb', 'cababcacab', 'cababcacac', 'cababcacba', 'cababcacbc', 'cababcbaba', 'cababcbabc', 'cababcbaca', 'cababcbacb', 'cababcbcab', 'cababcbcac', 'cababcbcba', 'cababcbcbc', 'cabacababa', 'cabacababc', 'cabacabaca', 'cabacabacb', 
                        'cabacabcab', 'cabacabcac', 'cabacabcba', 'cabacabcbc', 'cabacacaba', 'cabacacabc', 'cabacacaca', 'cabacacacb', 'cabacacbab', 'cabacacbac', 'cabacacbca', 'cabacacbcb', 'cabacbabab', 'cabacbabac', 'cabacbabca', 'cabacbabcb', 'cabacbacab', 'cabacbacac', 'cabacbacba', 'cabacbacbc', 
                        'cabacbcaba', 'cabacbcabc', 'cabacbcaca', 'cabacbcacb', 'cabacbcbab', 'cabacbcbac', 'cabacbcbca', 'cabacbcbcb', 'cabcababab', 'cabcababac', 'cabcababca', 'cabcababcb', 'cabcabacab', 'cabcabacac', 'cabcabacba', 'cabcabacbc', 'cabcabcaba', 'cabcabcabc', 'cabcabcaca', 'cabcabcacb', 
                        'cabcabcbab', 'cabcabcbac', 'cabcabcbca', 'cabcabcbcb', 'cabcacabab', 'cabcacabac', 'cabcacabca', 'cabcacabcb', 'cabcacacab', 'cabcacacac', 'cabcacacba', 'cabcacacbc', 'cabcacbaba', 'cabcacbabc', 'cabcacbaca', 'cabcacbacb', 'cabcacbcab', 'cabcacbcac', 'cabcacbcba', 'cabcacbcbc', 
                        'cabcbababa', 'cabcbababc', 'cabcbabaca', 'cabcbabacb', 'cabcbabcab', 'cabcbabcac', 'cabcbabcba', 'cabcbabcbc', 'cabcbacaba', 'cabcbacabc', 'cabcbacaca', 'cabcbacacb', 'cabcbacbab', 'cabcbacbac', 'cabcbacbca', 'cabcbacbcb', 'cabcbcabab', 'cabcbcabac', 'cabcbcabca', 'cabcbcabcb', 
                        'cabcbcacab', 'cabcbcacac', 'cabcbcacba', 'cabcbcacbc', 'cabcbcbaba', 'cabcbcbabc', 'cabcbcbaca', 'cabcbcbacb', 'cabcbcbcab', 'cabcbcbcac', 'cabcbcbcba', 'cabcbcbcbc', 'cacabababa', 'cacabababc', 'cacababaca', 'cacababacb', 'cacababcab', 'cacababcac', 'cacababcba', 'cacababcbc', 
                        'cacabacaba', 'cacabacabc', 'cacabacaca', 'cacabacacb', 'cacabacbab', 'cacabacbac', 'cacabacbca', 'cacabacbcb', 'cacabcabab', 'cacabcabac', 'cacabcabca', 'cacabcabcb', 'cacabcacab', 'cacabcacac', 'cacabcacba', 'cacabcacbc', 'cacabcbaba', 'cacabcbabc', 'cacabcbaca', 'cacabcbacb', 
                        'cacabcbcab', 'cacabcbcac', 'cacabcbcba', 'cacabcbcbc', 'cacacababa', 'cacacababc', 'cacacabaca', 'cacacabacb', 'cacacabcab', 'cacacabcac', 'cacacabcba', 'cacacabcbc', 'cacacacaba', 'cacacacabc', 'cacacacaca', 'cacacacacb', 'cacacacbab', 'cacacacbac', 'cacacacbca', 'cacacacbcb', 
                        'cacacbabab', 'cacacbabac', 'cacacbabca', 'cacacbabcb', 'cacacbacab', 'cacacbacac', 'cacacbacba', 'cacacbacbc', 'cacacbcaba', 'cacacbcabc', 'cacacbcaca', 'cacacbcacb', 'cacacbcbab', 'cacacbcbac', 'cacacbcbca', 'cacacbcbcb', 'cacbababab', 'cacbababac', 'cacbababca', 'cacbababcb', 
                        'cacbabacab', 'cacbabacac', 'cacbabacba', 'cacbabacbc', 'cacbabcaba', 'cacbabcabc', 'cacbabcaca', 'cacbabcacb', 'cacbabcbab', 'cacbabcbac', 'cacbabcbca', 'cacbabcbcb', 'cacbacabab', 'cacbacabac', 'cacbacabca', 'cacbacabcb', 'cacbacacab', 'cacbacacac', 'cacbacacba', 'cacbacacbc', 
                        'cacbacbaba', 'cacbacbabc', 'cacbacbaca', 'cacbacbacb', 'cacbacbcab', 'cacbacbcac', 'cacbacbcba', 'cacbacbcbc', 'cacbcababa', 'cacbcababc', 'cacbcabaca', 'cacbcabacb', 'cacbcabcab', 'cacbcabcac', 'cacbcabcba', 'cacbcabcbc', 'cacbcacaba', 'cacbcacabc', 'cacbcacaca', 'cacbcacacb', 
                        'cacbcacbab', 'cacbcacbac', 'cacbcacbca', 'cacbcacbcb', 'cacbcbabab', 'cacbcbabac', 'cacbcbabca', 'cacbcbabcb', 'cacbcbacab', 'cacbcbacac', 'cacbcbacba', 'cacbcbacbc', 'cacbcbcaba', 'cacbcbcabc', 'cacbcbcaca', 'cacbcbcacb', 'cacbcbcbab', 'cacbcbcbac', 'cacbcbcbca', 'cacbcbcbcb', 
                        'cbabababab', 'cbabababac', 'cbabababca', 'cbabababcb', 'cbababacab', 'cbababacac', 'cbababacba', 'cbababacbc', 'cbababcaba', 'cbababcabc', 'cbababcaca', 'cbababcacb', 'cbababcbab', 'cbababcbac', 'cbababcbca', 'cbababcbcb', 'cbabacabab', 'cbabacabac', 'cbabacabca', 'cbabacabcb', 
                        'cbabacacab', 'cbabacacac', 'cbabacacba', 'cbabacacbc', 'cbabacbaba', 'cbabacbabc', 'cbabacbaca', 'cbabacbacb', 'cbabacbcab', 'cbabacbcac', 'cbabacbcba', 'cbabacbcbc', 'cbabcababa', 'cbabcababc', 'cbabcabaca', 'cbabcabacb', 'cbabcabcab', 'cbabcabcac', 'cbabcabcba', 'cbabcabcbc', 
                        'cbabcacaba', 'cbabcacabc', 'cbabcacaca', 'cbabcacacb', 'cbabcacbab', 'cbabcacbac', 'cbabcacbca', 'cbabcacbcb', 'cbabcbabab', 'cbabcbabac', 'cbabcbabca', 'cbabcbabcb', 'cbabcbacab', 'cbabcbacac', 'cbabcbacba', 'cbabcbacbc', 'cbabcbcaba', 'cbabcbcabc', 'cbabcbcaca', 'cbabcbcacb', 
                        'cbabcbcbab', 'cbabcbcbac', 'cbabcbcbca', 'cbabcbcbcb', 'cbacababab', 'cbacababac', 'cbacababca', 'cbacababcb', 'cbacabacab', 'cbacabacac', 'cbacabacba', 'cbacabacbc', 'cbacabcaba', 'cbacabcabc', 'cbacabcaca', 'cbacabcacb', 'cbacabcbab', 'cbacabcbac', 'cbacabcbca', 'cbacabcbcb', 
                        'cbacacabab', 'cbacacabac', 'cbacacabca', 'cbacacabcb', 'cbacacacab', 'cbacacacac', 'cbacacacba', 'cbacacacbc', 'cbacacbaba', 'cbacacbabc', 'cbacacbaca', 'cbacacbacb', 'cbacacbcab', 'cbacacbcac', 'cbacacbcba', 'cbacacbcbc', 'cbacbababa', 'cbacbababc', 'cbacbabaca', 'cbacbabacb', 
                        'cbacbabcab', 'cbacbabcac', 'cbacbabcba', 'cbacbabcbc', 'cbacbacaba', 'cbacbacabc', 'cbacbacaca', 'cbacbacacb', 'cbacbacbab', 'cbacbacbac', 'cbacbacbca', 'cbacbacbcb', 'cbacbcabab', 'cbacbcabac', 'cbacbcabca', 'cbacbcabcb', 'cbacbcacab', 'cbacbcacac', 'cbacbcacba', 'cbacbcacbc', 
                        'cbacbcbaba', 'cbacbcbabc', 'cbacbcbaca', 'cbacbcbacb', 'cbacbcbcab', 'cbacbcbcac', 'cbacbcbcba', 'cbacbcbcbc', 'cbcabababa', 'cbcabababc', 'cbcababaca', 'cbcababacb', 'cbcababcab', 'cbcababcac', 'cbcababcba', 'cbcababcbc', 'cbcabacaba', 'cbcabacabc', 'cbcabacaca', 'cbcabacacb', 
                        'cbcabacbab', 'cbcabacbac', 'cbcabacbca', 'cbcabacbcb', 'cbcabcabab', 'cbcabcabac', 'cbcabcabca', 'cbcabcabcb', 'cbcabcacab', 'cbcabcacac', 'cbcabcacba', 'cbcabcacbc', 'cbcabcbaba', 'cbcabcbabc', 'cbcabcbaca', 'cbcabcbacb', 'cbcabcbcab', 'cbcabcbcac', 'cbcabcbcba', 'cbcabcbcbc', 
                        'cbcacababa', 'cbcacababc', 'cbcacabaca', 'cbcacabacb', 'cbcacabcab', 'cbcacabcac', 'cbcacabcba', 'cbcacabcbc', 'cbcacacaba', 'cbcacacabc', 'cbcacacaca', 'cbcacacacb', 'cbcacacbab', 'cbcacacbac', 'cbcacacbca', 'cbcacacbcb', 'cbcacbabab', 'cbcacbabac', 'cbcacbabca', 'cbcacbabcb', 
                        'cbcacbacab', 'cbcacbacac', 'cbcacbacba', 'cbcacbacbc', 'cbcacbcaba', 'cbcacbcabc', 'cbcacbcaca', 'cbcacbcacb', 'cbcacbcbab', 'cbcacbcbac', 'cbcacbcbca', 'cbcacbcbcb', 'cbcbababab', 'cbcbababac', 'cbcbababca', 'cbcbababcb', 'cbcbabacab', 'cbcbabacac', 'cbcbabacba', 'cbcbabacbc', 
                        'cbcbabcaba', 'cbcbabcabc', 'cbcbabcaca', 'cbcbabcacb', 'cbcbabcbab', 'cbcbabcbac', 'cbcbabcbca', 'cbcbabcbcb', 'cbcbacabab', 'cbcbacabac', 'cbcbacabca', 'cbcbacabcb', 'cbcbacacab', 'cbcbacacac', 'cbcbacacba', 'cbcbacacbc', 'cbcbacbaba', 'cbcbacbabc', 'cbcbacbaca', 'cbcbacbacb', 
                        'cbcbacbcab', 'cbcbacbcac', 'cbcbacbcba', 'cbcbacbcbc', 'cbcbcababa', 'cbcbcababc', 'cbcbcabaca', 'cbcbcabacb', 'cbcbcabcab', 'cbcbcabcac', 'cbcbcabcba', 'cbcbcabcbc', 'cbcbcacaba', 'cbcbcacabc', 'cbcbcacaca', 'cbcbcacacb', 'cbcbcacbab', 'cbcbcacbac', 'cbcbcacbca', 'cbcbcacbcb', 
                        'cbcbcbabab', 'cbcbcbabac', 'cbcbcbabca', 'cbcbcbabcb', 'cbcbcbacab', 'cbcbcbacac', 'cbcbcbacba', 'cbcbcbacbc', 'cbcbcbcaba', 'cbcbcbcabc', 'cbcbcbcaca', 'cbcbcbcacb', 'cbcbcbcbab', 'cbcbcbcbac', 'cbcbcbcbca', 'cbcbcbcbcb']


        return ans[k] if k < len(ans) else ''
