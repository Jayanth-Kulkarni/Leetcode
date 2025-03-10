class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        sd, pd = defaultdict(int), defaultdict(int)
        l = 0
        res = []
        for i in p:
            pd[i] += 1
        for r in range(len(p)):
            sd[s[r]] += 1
        if sd == pd:
            res.append(0)
        for r in range(len(p), len(s)):
            sd[s[r]] += 1
            sd[s[l]] -= 1
            if sd[s[l]] == 0:
                del sd[s[l]]
            l += 1
            if sd == pd:
                res.append(l)
        return res