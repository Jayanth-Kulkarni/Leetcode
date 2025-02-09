class TrieNode:
    def __init__(self):
        self.children = {}
        self.eos = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        t = self.trie
        for s in word:
            if s not in t.children:
                t.children[s] = TrieNode()
            t = t.children[s]
        t.eos = True

    def search(self, word: str) -> bool:
        t = self.trie
        for s in word:
            if s not in t.children:
                return False
            t = t.children[s]
        return t.eos      

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for s in prefix:
            if s not in t.children:
                return False
            t = t.children[s]
        return True    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)