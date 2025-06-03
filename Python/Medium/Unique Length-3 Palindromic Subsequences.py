'''
Observations:
for a palindrome, first and third letters MUST be equal, second letter can be anything

My solution after seeing the editorial:
TC: O(N). 27 linear passes over the string at the most.
SC: O(1). The dictionary and set only every reach a max length of 26, which is O(1).
'''
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Get the first and last indices of each letter
        first_last_indices = defaultdict(lambda: [-1, 0])
        for idx, char in enumerate(s):
            if first_last_indices[char][0] == -1:
                first_last_indices[char][0] = first_last_indices[char][1] = idx
            else:
                first_last_indices[char][1] = idx

        # For each letter, find how many unique chars are in between them
        # manually by just iterating through the string
        # Iterating is O(N), but will be performed max 26 times, so O(N) overall
        ans = 0
        for letter in first_last_indices:
            left, right = first_last_indices[letter]
            unique = set()
            for i in range(left + 1, right):
                unique.add(s[i])
            ans += len(unique)

        return ans

'''
abcdcbaxyzyxa

a bcdcb a xyzyx a

aba
aca
ada
axa
aya
aza
aaa

bcb
bdb
cdc

xyx
xzx
yzy

=> 13
'''
