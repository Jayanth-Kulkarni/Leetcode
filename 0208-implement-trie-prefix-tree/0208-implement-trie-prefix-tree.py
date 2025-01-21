class TrieNode:
    def __init__(self):
        self.children = {}
        self.eos = False
class Trie:
    def __init__(self):
        self.trie = TrieNode()        

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie.children:
                trie.children[letter] = TrieNode()                
            trie = trie.children[letter]
        trie.eos = True
        return

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter in trie.children:
                trie = trie.children[letter]
            else:
                return False 
        return trie.eos

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter in trie.children:
                trie = trie.children[letter]
            else:
                return False 
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)