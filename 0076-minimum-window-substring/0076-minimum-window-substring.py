class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td, win = {}, {}
        for i in t:
            td[i] = 1 + td.get(i, 0)
        need, have = len(td), 0
        l = 0
        res = [-1,-1]
        reslen = float("inf")
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c, 0)

            if c in td and win[c] == td[c]:
                have += 1
            
            while need == have:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l,r]
                c = s[l]
                win[c] -= 1

                if c in td and win[c] < td[c]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""