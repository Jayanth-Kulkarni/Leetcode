class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td, sd = {}, {}
        l, r = 0, 0
        res, reslen = [-1,-1], float("inf")
        for i in t:
            td[i] = 1 + td.get(i, 0)
        
        need, have = len(td), 0
        # print(need, have)
        
        for r in range(len(s)):
            i = s[r]
            sd[i] = 1 + sd.get(i, 0)

            if i in td and td[i] == sd[i]:
                have += 1        

            # print(sd, td, l, r)
            while need == have:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = [l, r]

                j = s[l]
                sd[j] -= 1

                if j in td and td[j] > sd[j]:
                    have -= 1
            
                l += 1
        
        l, r = res
        if reslen != float("inf"):
            return s[l: r+1]
        
        return ""