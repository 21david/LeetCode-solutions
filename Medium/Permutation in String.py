# https://leetcode.com/problems/permutation-in-string/

# Sliding window
class Solution:
    def checkInclusion(self, s: str, long_word: str) -> bool:
        L = len(long_word)
        s_count = Counter(s)
        window = {}
        l = r = 0

        while r < L:
            new_char = long_word[r]
            if new_char in s_count:
                # Try to form a window that is a permutation
                window[new_char] = window.get(new_char, 0) + 1
                while window[new_char] > s_count[new_char]:
                    # If too many of letter c, remove letters until same number of cs
                    lc = long_word[l]
                    window[lc] -= 1
                    if window[lc] == 0:
                        del window[lc]
                        # break
                    l += 1
                if window == s_count:
                    # If all counts match exactly, this is a permutation
                    return True
                r += 1
            else:
                # Can't be a permutation, so start over with next letter
                window.clear()
                r += 1
                l = r

        return False
