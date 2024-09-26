'''
https://leetcode.com/problems/longest-word-with-all-prefixes/description/?envType=weekly-question&envId=2024-09-22  (Premium)

Put all words in a trie. Then do a DFS on the trie, only going deeper for
each node that is marked as the end of the word. This will cause it to only
visit words that have every prefix in the trie. To handle the lexigographical
requirement, we store the word that breaks the record in a variable. The DFS
will need to visit words in lexigographical order starting from a and ending in z.
If we only update the word when the record is broken, then the leftmost word
(lexigographically smallest one) will be stored as the max.

TC should be O(m) where m is the number of letters in the array.
or O(w * l) where w is the number of words, and l is the length of the
average word length. 

SC should also be O(m), or O(w * l).

l can also represent the length of the longest word length, but this isn't as
tight of a bound. My thinking behind this is that if l is the length of the
average word (all lengths averaged out), then w * l == the total number of
characters.
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Store all words in a trie
        trie_head = {}
        for word in words:
            ptr = trie_head
            # Add word to trie
            for c in word:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]  # Move to the child (letter)
            # Once done processing a whole word, mark the node as word-ending
            ptr['*'] = {}  # this will represent a word end. Any non-letter also works.

        # DFS to find the deepest path of consecutive word-ending nodes
        max_word = ''

        def dfs(ptr, curr_word):
            nonlocal max_word
            for char, dic in sorted(ptr.items()):
                if '*' not in dic:
                    continue  # This is not the end of some word
                curr_word.append(char)
                if len(curr_word) > len(max_word):
                    max_word = ''.join(curr_word)
                dfs(dic, curr_word)
                curr_word.pop()

        dfs(trie_head, [])
        return max_word


'''
Iterative DFS approach
'''
# Trie Node
class Node:
    def __init__(self, letter=None, end=False, parent=None, depth=0):
        self.letter = letter
        self.end = end
        self.parent = parent
        self.depth = depth
        self.links = [None] * 26

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Store all words in a trie
        trie = Node()
        for word in words:
            ptr = trie
            for c in word:
                pos = ord(c) - 97
                if not ptr.links[pos]:
                    ptr.links[pos] = Node(letter=c, parent=ptr, depth=ptr.depth+1)
                ptr = ptr.links[pos]
            ptr.end = True  # Mark this node as word-ending

        # DFS to find the deepest path of consecutive word-ending nodes
        max_depth_node = trie
        stack = [trie]
        while stack:
            node = stack.pop()
            if node.depth > max_depth_node.depth:
                max_depth_node = node

            for next_node in reversed(node.links):
                if next_node and next_node.end:
                    stack.append(next_node)

        # If no word was found, return empty string
        if max_depth_node == trie:
            return ''

        # If a word was found, construct it using the nodes
        answer = deque([])
        ptr = max_depth_node
        while ptr:
            if ptr.letter:
                answer.appendleft(ptr.letter)
            ptr = ptr.parent

        return ''.join(answer)
