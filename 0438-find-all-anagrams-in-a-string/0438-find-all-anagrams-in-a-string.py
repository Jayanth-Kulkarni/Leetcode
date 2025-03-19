class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        dp, ds = defaultdict(int), defaultdict(int)
        res = []
        l = 0
        for i in p:
            dp[i] += 1
        for i in s[:len(p)]:
            ds[i] += 1
        if ds == dp:
            res.append(0)
        for r in range(len(p), len(s)):
            ds[s[l]] -= 1
            if ds[s[l]] == 0:
                del ds[s[l]]
            ds[s[r]] += 1
            l += 1
            if ds == dp:
                res.append(l)
        return res