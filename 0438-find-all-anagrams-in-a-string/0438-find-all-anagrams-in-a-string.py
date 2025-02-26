class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        cur = defaultdict(int)
        tar = defaultdict(int)
        res = []
        for i in range(len(p)):
            cur[s[i]] += 1
        for i in range(len(p)):
            tar[p[i]] += 1
        if cur == tar:
            res.append(0)
        
        l, r = 0, len(p)
        while l < r < len(s):
            cur[s[l]] -= 1
            if cur[s[l]] == 0:
                del cur[s[l]]
            l += 1
            cur[s[r]] += 1
            if cur == tar:
                res.append(l)
            r += 1
        return res