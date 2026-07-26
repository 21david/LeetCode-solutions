class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        ans = ['0'] * n

        i = 0
        while s:
            if i >= len(ans): break
                
            if s > 9:
                ans[i] = '9'
                s -= 9
            else:
                ans[i] = str(s)
                s -= s
                break
            i += 1

        if s:
            return -1  # couldnt reach sum of s even with all 9s
        else:
            return int(''.join(ans))©leetcode
