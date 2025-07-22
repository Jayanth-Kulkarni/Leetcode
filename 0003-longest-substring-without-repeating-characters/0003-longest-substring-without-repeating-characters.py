class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        cur = set()
        while l <= r < len(s):
            if s[r] not in cur:
                cur.add(s[r])
                res = max(res,len(cur))
                r += 1
            else:
                cur.remove(s[l])
                l += 1
        return res