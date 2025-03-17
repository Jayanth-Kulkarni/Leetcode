class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = [False for i in range(len(s)+1)]
        d[len(s)] = True
        for i in range(len(s), -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    d[i] = d[i+len(word)]
                if d[i]:
                    break
        return d[0]