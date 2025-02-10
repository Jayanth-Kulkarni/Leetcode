class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while need == have:
                if r-l+1 < resLen:
                    resLen = r-l+1
                    res = [l, r]
                d = s[l]
                window[d] -= 1

                if d in countT and window[d] < countT[d]:
                    have -= 1
                l += 1
        
        l, r = res
        if resLen != float("inf"):
            return s[l:r+1]

        return ""
                
