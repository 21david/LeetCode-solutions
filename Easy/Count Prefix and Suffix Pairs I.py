class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix_and_suffix(a, b):
            return b.startswith(a) and b.endswith(a)

        N = len(words)
        count = 0
        for i in range(N-1):
            for j in range(i+1, N):
                count += is_prefix_and_suffix(words[i], words[j])

        return count
