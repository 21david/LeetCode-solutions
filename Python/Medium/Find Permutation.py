class Solution:
    def findPermutation(self, s: str) -> List[int]:
        ans = [n for n in range(1, len(s) + 2)]

        # For every set of letters like DDDI (at least one D followed by one I)
        # reverse that range of indices

        i = 0
        S = len(s)
        while i < S:
            if s[i] == 'D':
                start = i
                j = i + 1
                while (j < S and s[j] == "D"):
                    j += 1
                dist = (j + 1 - start)
                # Reverse
                ans[start:j+1] = ans[start:j+1][::-1]
                i = j
            i += 1

        return ans

'''
Solved after skimming editorial
DDDII
4 3 2 1 _ _

1 2 3 4


DDDIIDDIDIII

4 3 2 1 5

DDD
4 3 2 1

I I D D D
1 2 6 5 4 3


IIIDIDI

1 2 3 5 4 7 6 8

I I I D D D D D I  I  D  D  I
1 2 3 9 8 7 6 5 4 10 13 12 11 14

  I I I D D D D D  I  I  D  D  I
1 2 3 4 5 6 7 8 9 10 11 12 13 14

10 11
1 2 3 9 8 7 6 5 4

'''
