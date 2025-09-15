# TC = O(T + B)
# SC = O(T + B)
# T = length of text, B = length of brokenLetters
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        count = 0

        for word in text.split():
            count += all(ch not in broken for ch in word)

        return count

# One line
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(all(ch not in brokenLetters for ch in word) for word in text.split())
