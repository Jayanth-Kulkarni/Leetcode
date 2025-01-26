class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r, cur, res = 0, 1, [s[0]], 1
        while l < r < len(s):
            if s[r] not in cur:
                cur.append(s[r])
                res = max(res, len(cur))
            else:
                while 0 <= l < r < len(s) and s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1

                while 0 <= l < r < len(s) and s[l] == s[r]:
                    l += 1
            
            r += 1
        return res 