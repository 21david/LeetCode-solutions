# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Node:
    def __init__(self):
        # Marks if the current node is the end of a word
        self.end = False

        # letter-Node pairs like {'a': [Node], 'm': [Node], 'z': [Node]}
        self.nexts = {}

class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        temp = self.head
        for c in word:
            if c not in temp.nexts:
                temp.nexts[c] = Node()
            temp = temp.nexts[c]
        temp.end = True

    def search(self, word: str) -> bool:
        temp = self.head
        for c in word:
            if c in temp.nexts:
                temp = temp.nexts[c]
            else:
                return False
        return temp.end

    def startsWith(self, prefix: str) -> bool:
        temp = self.head
        for c in prefix:
            if c in temp.nexts:
                temp = temp.nexts[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
