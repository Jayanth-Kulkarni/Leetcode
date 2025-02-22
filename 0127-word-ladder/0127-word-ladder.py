class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(list)
        q = deque()
        q.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                d[s].append(word)
        res = 1
        visited = set()
        visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i+1:]
                    for nei in d[s]:
                        if nei not in visited:
                            q.append(nei)
                            visited.add(nei)
            res += 1
        
        return 0