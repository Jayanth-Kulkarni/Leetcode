class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Trie:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.node
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isend = True
        return

    def search(self, word: str) -> bool:
        cur = self.node
        for letter in word:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return cur.isend

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)