# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right

# After seeing text part of editorial - sliding window
# Invert the problem - how big of a window can you take out such that
# outside the window, the conditions still hold
# Instead of the minimum you can keep, ask the maximum you can get rid of
# Then use sliding window to find that maximum
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        counts = Counter(s)

        if k == 0:
            return 0
        if len(counts) < 3 or any(count < k for count in counts.values()):
            return -1

        # Maximum we can remove of each letter before window becomes invalid
        # meaning outside the window, there aren't at least k of each letter anymore
        # and we have to start over with a new window
        max_remove = [0, 0, 0]  # [a, b, c]
        for letter, count in counts.items():
            max_remove[ord(letter) - 97] = count - k

        S = len(s)
        l = r = 0
        max_window = 0
        removed = [0, 0, 0]
        # Move right pointer to find biggest valid window
        while r < S:
            curr_letter = ord(s[r]) - 97
            removed[curr_letter] += 1
            if removed[curr_letter] > max_remove[curr_letter]:
                max_window = max(max_window, r - l)
                while removed[curr_letter] > max_remove[curr_letter]:
                    # When window is no longer valid,
                    # move left pointer until valid again
                    oldest_letter = ord(s[l]) - 97
                    removed[oldest_letter] -= 1
                    l += 1
            r += 1
        
        max_window = max(max_window, r - l)
                
        return S - max_window
