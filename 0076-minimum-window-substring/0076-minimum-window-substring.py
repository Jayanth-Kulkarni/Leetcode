class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, dt, ds = 0, defaultdict(int), defaultdict(int)
        reslen, res = float("inf"), ""
        for i in t:
            dt[i] += 1
        have, want = 0, len(dt)
        for r in range(len(s)):
            cur = s[r]
            ds[cur] += 1

            if cur in dt and ds[cur] == dt[cur]:
                have += 1
            
            while have == want:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = s[l:r+1]
                
                curl = s[l]
                ds[curl] -= 1
                
                if ds[curl] == 0:
                    del ds[curl]
                
                if curl in dt and ds[curl] < dt[curl]:
                    have -= 1
                
                l += 1
        return res