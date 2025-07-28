class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wd = defaultdict(int)
        hd = defaultdict(int)
        l, want, have, reslen, res = 0, 0, 0, float("inf"), [-1,-1]
        for i in t:
            wd[i] += 1
        want = len(wd)
        for r in range(len(s)):
            cur = s[r]
            hd[cur] += 1
            if cur in wd and hd[cur] == wd[cur]:
                have += 1
            while have == want:
                if r-l+1 < reslen:
                    reslen = r-l+1
                    res = [l, r]
                
                left = s[l]
                hd[left] -= 1
                if left in wd and hd[left] < wd[left]:
                    have -= 1
                l += 1
        
        l, r = res
        if reslen == float("inf"):
            return ""
        return s[l:r+1]