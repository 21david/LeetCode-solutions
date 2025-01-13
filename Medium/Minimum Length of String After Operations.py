# TC = SC = O(N)
class Solution:
    def minimumLength(self, s: str) -> int:
        freqs = Counter(s)
        removed = 0
        for _, count in freqs.items():
            if count >= 3:
                removed += (count - 1) // 2 * 2
        
        return len(s) - removed
