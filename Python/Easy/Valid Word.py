class Solution:
    def isValid(self, word: str) -> bool:
        vowels = set(list('aeiouAEIOU'))
        return len(word) >= 3  \
                and word.isalnum() \
                and any(c in vowels for c in word) \
                and any((c not in vowels and not c.isdigit()) for c in word)  # consonant
