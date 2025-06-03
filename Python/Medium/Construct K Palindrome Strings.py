'''
To construct a palindrome, you can use a single letter, followed by any number 
of pairs of any letter (abcxcba), or just any number of pairs of any letter (abccba).

If we take the frequency of all letters in s, we can determine the answer by looking 
at the parities of each letter.

If k is 3, we can have at most 3 odd frequencies, because if we have more, then we wouldn't
be able to put that single letter anywhere. For all the even frequencies, we can put them on
any of the 3 palindromes.

Approach:
Take frequencies of every letter.
Count how many frequencies are odd.
Compare that with k and return the result.

TC: O(N) to count frequencies with a hashmap, and to count odd frequencies
SC: O(1), the hash map will only grow to a size of 26 at the most.
'''
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s): return False
        frequencies = Counter(s)
        odds = sum(frequency % 2 == 1 for letter, frequency in frequencies.items())
        return odds <= k



# Same solution in one line
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return k <= len(s) and sum(frequency % 2 == 1 for letter, frequency in Counter(s).items()) <= k
