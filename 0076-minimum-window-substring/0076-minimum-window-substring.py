class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have = l = r = 0
        res = float("inf")
        res_list = [-1,-1]
        hc = defaultdict(int)
        nc = defaultdict(int)
        for i in t:
            nc[i] += 1
        need = len(nc)
        for r in range(len(s)):
            cur = s[r]
            hc[cur] += 1
            if cur in nc and hc[cur] == nc[cur]:
                have += 1
            while have == need:
                if r-l+1 < res:
                    res = r-l+1
                    res_list = [r,l]
                prev = s[l]
                hc[prev] -= 1
                if prev in nc and nc[prev] > hc[prev]:
                    have-= 1
                l+=1
        
        r, l = res_list
        return s[l:r+1] if res != float("inf") else ""