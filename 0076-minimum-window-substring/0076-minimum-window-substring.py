from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "" or t == "":
            return ""
        l, r, window, td = 0, 0, {}, {}
        for i in t:
            td[i] = 1 + td.get(i, 0)
        
        have, want = 0, len(td)
        res, resLen = float("inf"), [-1, -1]
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in td and window[c] == td[c]:
                have += 1  

            while have == want:
                if (r - l + 1) < res:
                    res = (r - l + 1)
                    resLen = [l, r]

                lc = s[l]
                window[lc] -= 1

                if lc in td and window[lc] < td[lc]:
                    have -= 1  
                
                l += 1

            r += 1
        
        return s[resLen[0] : resLen[1]+1] if res != float("inf") else ""