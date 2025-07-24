class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l, r , res, cur_max = 0, 0, 0, 0
        for r in range(len(s)):
            d[s[r]] += 1
            cur_max = max(d[s[r]], cur_max)
        
            if cur_max + k < r-l+1:
                d[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        return res