class Solution:
    def processStr(self, s: str) -> str:
        ans = []

        for c in s:
            match c:
            if c.isalpha():
                ans.append(c)
            elif len(ans) == 0:
                continue
            elif c == '*':
                ans.pop()
            elif c == '#':
                ans.extend([*ans])
            elif c == '%':
                ans.reverse()

        return ''.join(ans)
