class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append(beginWord)
        d = defaultdict(list)
        visited = set()
        res = 1
        for word in wordList:
            for i in range(0,len(word)):
                pat = word[:i] + "*" + word[i+1:]
                d[pat].append(word)
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(0, len(word)):
                    pat = word[:i] + "*" + word[i+1:]
                    for p in d[pat]:
                        if p not in visited:
                            q.append(p)
                            visited.add(p)
            if len(q) > 0:
                res += 1
        return 0