class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        ct = 0
        b = bin(n)[2:]
        n = len(b)
        
        for i in range(n-1):
            if b[i] == b[i+1] == '1':
                ct += 1

        return ct == 1
