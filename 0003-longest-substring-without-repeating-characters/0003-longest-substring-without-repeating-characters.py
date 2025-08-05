class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        l,r,res = 0,0,0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l+=1
            cur.add(s[r])
            res = max(res,r-l+1)
        return res