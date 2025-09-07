class Solution:
    def minOperations(self, s: str) -> int:
        a = sorted(list(set(s) - set('a')))
        a = [(ord('z') - ord(ch) + 1) for ch in a]
        a.append(0)
        ans = 0
        for i in range(len(a)-1):
            ans += a[i] - a[i+1]
        return ans©leetcode
