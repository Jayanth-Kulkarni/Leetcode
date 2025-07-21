class Solution:
    def minWindow(self, s: str, t: str) -> str:
        wd, hd = defaultdict(int), defaultdict(int)
        res_len = float("inf")
        res = [-1, -1]
        for i in t:
            wd[i] += 1
        want = len(wd)
        have, l = 0, 0
        for r in range(len(s)):
            cur = s[r]
            hd[cur] += 1
            if cur in wd and hd[cur] == wd[cur]:
                have += 1

            while have == want:
                if res_len > r-l+1:
                    res_len = r-l+1
                    res = [l, r]
                left = s[l]
                hd[left] -= 1
                if left in wd and hd[left] < wd[left]:
                    have -= 1
                l += 1
            
        if res_len == float("inf"):
            return ""
        
        l, r = res

        return s[l:r+1]