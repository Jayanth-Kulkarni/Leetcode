class TrieNode:
    def __init__(self):
        self.children = {}
        self.eos = False

class Trie:

    def __init__(self):
        self.t = TrieNode()

    def insert(self, word: str) -> None:
        t = self.t
        for i in word:
            if i not in t.children:
                t.children[i] = TrieNode()
            t = t.children[i]
        t.eos = True

    def search(self, word: str) -> bool:
        t = self.t
        for i in word:
            if i not in t.children:
                return False
            t = t.children[i]
        return t.eos

    def startsWith(self, prefix: str) -> bool:
        t = self.t
        for i in prefix:
            if i not in t.children:
                return False
            t = t.children[i]
        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)