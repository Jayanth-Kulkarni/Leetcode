class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td, sd = defaultdict(int), defaultdict(int)
        for i in t:
            td[i] += 1
        l, r = 0, 0
        reslen = float("inf")
        res = [-1,-1]
        want, have = len(td), 0
        for r in range(len(s)):
            cur = s[r]
            sd[cur] += 1
            if cur in td and sd[cur] == td[cur]:
                have += 1
            while want == have:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = s[l:r+1]

                cl = s[l]
                sd[cl] -= 1
                
                if sd[cl] == 0:
                    del sd[cl]
                
                if cl in td and sd[cl] < td[cl]:
                    have -= 1
                l += 1
            
        if reslen == float("inf"):
            return ""
        
        return res