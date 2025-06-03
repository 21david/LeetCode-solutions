# https://leetcode.com/problems/hash-divided-string

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        # Divide into n/k sub strings
        n = len(s)
        subs = []
        for i in range(0, n, k):
            subs.append(s[i: i+k])

        # Compute the hash values
        result = []
        for sub in subs:
            sum = 0
            for c in sub:
                sum += ord(c) - 97
            
            the_char = chr((sum % 26) + 97)
            result.append(the_char)

        return ''.join(result)
