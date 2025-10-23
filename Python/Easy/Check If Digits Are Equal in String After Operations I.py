class Solution:
    def hasSameDigits(self, s: str) -> bool:
        orig = list(int(c) for c in s)
        temp = []

        def transform():
            nonlocal orig
            temp = [(orig[i] + orig[i-1]) % 10 for i in range(1, len(orig))]
            orig = temp
            temp = []

        transform()

        while len(orig) > 2:
            transform()

        return orig[0] == orig[1]
            
