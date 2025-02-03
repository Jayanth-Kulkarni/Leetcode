class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td, cd = {}, {}
        for i in t:
            td[i] = td.get(i, 0) + 1
        
        have, need, l = 0, len(td), 0
        res, reslen = float("inf"), [-1, -1]
        for r in range(len(s)):
            ele = s[r]
            cd[ele] = cd.get(ele, 0) + 1

            if ele in td and cd[ele] == td[ele]:
                have += 1

            while have == need:
                if res > (r-l+1):
                    res = r - l + 1
                    reslen = [l, r]
                
                cd[s[l]] -= 1
                if s[l] in td and cd[s[l]] < td[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = reslen
        return s[l:r+1] if res != float("inf") else ""