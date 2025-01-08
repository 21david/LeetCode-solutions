'''
Brute force approach

TC: O(N^2 * M). N is the number of words, M is the average length of the words.
SC: O(1)
'''
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


'''
Same approach in two statements
'''
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        N = len(words)
        return sum(
            words[j].startswith(words[i]) and words[j].endswith(words[i])
            for i in range(N-1)
            for j in range(i+1, N)
        )
