class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cd, td = defaultdict(int), defaultdict(int)
        for i in t:
            td[i] += 1
        
        have, need = 0, len(td)
        l = 0
        reslen, res = float("inf"), [-1,-1]
        
        for r in range(len(s)):
            c = s[r]
            cd[c] += 1

            if c in td and cd[c] == td[c]:
                have += 1
            
            while have == need:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = [l, r]
                a = s[l]
                cd[a] -= 1

                if a in td and cd[a] < td[a]:
                    have -= 1
                
                l += 1
        l,r = res
        return s[l:r+1] if reslen != float("-inf") else ""