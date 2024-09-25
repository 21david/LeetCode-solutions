"""
The approach here is to use a Trie. To build a Trie, we add each word to the Trie.
For each word, we expand the Trie as needed, adding each letter into it.
This involves adding a node for each letter. If the letter already exists, then we
increment a count variable on it. The end result is a Trie that has a node for 
every letter in every word in the correct orders. Each letter has a count, which 
represents how many prefixes end at that letter's node. 

To calculate the answer, we just need to pass in a word and take the sum of all the
counts of all the letters in that word. We repeat this for every word in the input
array and return an array of the sums.
"""

class TrieNode:
    def __init__(self, words=None):
        self.amount = 0
        self.nexts = [None] * 26  # pointers to TrieNode for each letter

        # If a list of words passed in, add them to the trie
        if words:
            for word in words:
                self.add(word)
    
    # Add a word to the trie, increasing the amount at each letter by 1
    # or setting it to 1 if it didn't already exist
    def add(self, word):
        self._add(word, 0)

    def _add(self, word, word_idx):
        if word_idx == len(word):  # after the last letter
            return

        letter_pos = ord(word[word_idx]) - 97
        if self.nexts[letter_pos] is None:
            self.nexts[letter_pos] = TrieNode()

        self.nexts[letter_pos].amount += 1
        self.nexts[letter_pos]._add(word, word_idx + 1)

    # Assumes word is in the trie
    # Travel down the path of a word, then sums all their amounts
    def get_sum(self, word):
        return self._get_sum(word, 0)
    
    def _get_sum(self, word, word_idx):
        if word_idx == len(word):  # after the last letter
            return self.amount

        letter_pos = ord(word[word_idx]) - 97
        return self.amount + self.nexts[letter_pos]._get_sum(word, word_idx + 1)

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Construct trie
        head = TrieNode(words)

        # Calculate answer
        return [head.get_sum(word) for word in words]

'''
Test cases:
["abc","ab","bc","b"]
["abcd"]
["a"]
["a","b","aa","ab"]

Test trie with input ["abc","ab","bc","b"]
# print(head.nexts[0].amount) # 2
# print(head.nexts[0].nexts[1].amount) # 2
# print(head.nexts[0].nexts[1].nexts[2].amount) # 1
# print(head.nexts[1].amount) # 2
# print(head.nexts[1].nexts[2].amount) # 1
# print(head.nexts[1].nexts[2].nexts) # Nones
print(head.get_sum('abc', 0))  # 5
'''
