class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append(beginWord)
        dc = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + "*" + word[i+1:]
                dc[s].append(word)
        res = 1
        visited = set()
        visited.add(beginWord)
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    s = word[:i] + "*" + word[i+1:]
                    for sub in dc[s]:
                        if sub not in visited:
                            queue.append(sub)
                            visited.add(sub)
            res += 1
        
        return 0