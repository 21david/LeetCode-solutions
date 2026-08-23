class Solution:
    def isPalindromic(self, s: str) -> bool:
        S = len(s)
        bina = []
        for c in s:
            curbina = bin(ord(c))[2:]
            while len(curbina) < 8:
                curbina = "0" + curbina
            
            bina.append(curbina)

        bina = ''.join(bina)
        return bina[:len(bina)//2] == ''.join(list(reversed(bina[len(bina)//2:])))
