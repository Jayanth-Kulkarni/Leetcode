class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt, cur = {}, {}
        for i in t:
            dt[i] = 1 + dt.get(i, 0)
        l, r = 0, 0
        res = float("inf")
        reslen = [-1, -1]
        need, have = len(dt), 0
        for r in range(len(s)):
            cur[s[r]] = 1 + cur.get(s[r],0)
            if s[r] in dt and cur[s[r]] == dt[s[r]]:
                have += 1
            while need == have:
                if res > (r - l + 1):
                    res = r - l + 1
                    reslen = [l, r]
                
                cur[s[l]] -= 1
                if s[l] in dt and cur[s[l]] < dt[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = reslen
        return  s[l:r+1] if res != float("inf") else ""
