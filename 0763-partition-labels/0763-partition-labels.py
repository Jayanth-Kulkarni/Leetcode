class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        for idx, i in enumerate(s):
            d[i] = idx
        start = end = 0
        result = []
        for i, char in enumerate(s):
            end = max(d[char], end)
            print(char, end)
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result