class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        ans = 0
        for st in words:
            rev = st[1] + st[0]
            if rev in seen:
                seen[rev] -= 1
                if seen[rev] == 0:
                    del seen[rev]
                ans += 4
            else:
                seen[st] += 1

        # Check for a pair of two repeated characters in seen 
        # which may be used as the middle, such as 'xx'
        ans += 2 * any(st[0] == st[1] for st in seen)

        return ans

