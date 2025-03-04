class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []
        cur = defaultdict(int)
        tar = defaultdict(int)
        l = 0
        for i in p:
            tar[i] += 1
        for r in range(0, len(p)):
            cur[s[r]] += 1
        if cur == tar:
            res.append(l)
        for r in range(len(p), len(s)):
            cur[s[r]] += 1
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
            l += 1
            if cur == tar:
                res.append(l)
        return res