class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queuedict = defaultdict(list)
        wordList.append(beginWord)
        res = 1
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                queuedict[s].append(word)
        print(queuedict)
        visit = set([beginWord])
        q = deque([beginWord])
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    s = word[:j] + "*" + word[j+1:]
                    for nei in queuedict[s]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            res += 1
        return 0