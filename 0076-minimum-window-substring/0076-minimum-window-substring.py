class Solution:
    def minWindow(self, s: str, t: str) -> str:
        want, have, l = 0, 0, 0
        reslen = float("inf")
        res = [-1, -1]
        wd, hd = defaultdict(int), defaultdict(int)
        for char in t:
            wd[char] += 1
        want = len(wd)
        for r in range(len(s)):
            cur = s[r]
            hd[cur] += 1
            if cur in wd and hd[cur] == wd[cur]:
                have += 1
            print(cur, have, reslen, res)
            while have == want:
                if reslen > r-l+1:
                    reslen = r-l+1
                    res = [l, r]
                left = s[l]
                hd[left] -= 1
                if left in wd and hd[left] < wd[left]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if reslen != float("inf") else ""
        