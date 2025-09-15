# TC = O(T)
# SC = O(T)
# T = length of text
# brokenLetters is constrained to the 26 letters, so it is O(1)
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
