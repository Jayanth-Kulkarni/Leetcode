class TrieNode:
    def __init__(self):
        self.trie = {}
        self.eos = False

class Trie:

    def __init__(self):
        self.prefix = TrieNode()

    def insert(self, word: str) -> None:
        trie = self.prefix
        for s in word:
            if s not in trie.trie:
                trie.trie[s] = TrieNode()
            trie = trie.trie[s]
        trie.eos = True


    def search(self, word: str) -> bool:
        trie = self.prefix
        for s in word:
            if s not in trie.trie:
                return False
            trie = trie.trie[s]
        return trie.eos

    def startsWith(self, prefix: str) -> bool:
        trie = self.prefix
        for s in prefix:
            if s not in trie.trie:
                return False
            trie = trie.trie[s]
        return True       


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)