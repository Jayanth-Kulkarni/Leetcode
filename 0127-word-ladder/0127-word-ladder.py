class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queuedict = defaultdict(list)
        wordList.append(beginWord)
        res = 1
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                queuedict[s].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    s = word[:j] + "*" + word[j+1:]
                    for neiword in queuedict[s]:
                        if neiword not in visit:
                            visit.add(neiword)
                            q.append(neiword)
            res += 1
        return 0