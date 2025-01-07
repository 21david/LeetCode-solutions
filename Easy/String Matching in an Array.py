# Brute force
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, word in enumerate(words):
            for prev_word in words:
                if word in prev_word and word != prev_word:
                    ans.append(word)
                    break
                    
        return ans
