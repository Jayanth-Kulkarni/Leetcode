class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        l, r = 0, len(p)-1
        res = []
        cur = defaultdict(int)
        target = defaultdict(int)
        for i in range(r+1):
            target[p[i]] += 1
        for i in range(r+1):
            cur[s[i]] += 1
        if cur == target:
            res.append(0)
        r += 1
        while 0 <= l < r < len(s):
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
            l += 1
            cur[s[r]] += 1
            if cur == target:
                res.append(l)
            r+=1
        return res