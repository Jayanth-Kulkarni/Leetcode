class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l = 0

        td, window = {}, {}
        res, resLen = [-1,-1], float("inf")
        for i in t:
            td[i] = 1 + td.get(i, 0)
        have, want = 0, len(td)
        for r in range(len(s)):
            i = s[r]
            window[i] = 1 + window.get(i, 0)
            
            if i in td and window[i] == td[i]:
                have += 1
            
            while have == want:
                j = s[l]
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]

                window[j] -= 1
                
                if j in td and window[j] < td[j]:
                    have -= 1                
                l += 1

        if resLen == float("inf"):
            return ""

        l, r = res
        return s[l:r+1]
            