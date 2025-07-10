class Solution:
    def minWindow(self, s: str, t: str) -> str:
        want_dict, have_dict = defaultdict(int), defaultdict(int)
        
        for i in t:
            want_dict[i] += 1
        
        want, have, l, res, res_val = len(want_dict), 0, 0, float("inf"), [-1,-1]
        
        for r in range(len(s)):
            cur = s[r]
            have_dict[cur] += 1
            if cur in want_dict and have_dict[cur] == want_dict[cur]:
                have += 1
            while have == want:
                if res > r-l+1:
                    res = r-l+1
                    res_val = [l, r]
                left = s[l]
                have_dict[left] -= 1
                if left in want_dict and have_dict[left] < want_dict[left]:
                    have -= 1
                l+=1
        l, r = res_val
        return s[l:r+1] if res != float("inf") else ""
