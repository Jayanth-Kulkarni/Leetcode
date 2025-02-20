class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
             return 0
        l, r = 0, 1
        cur = [s[0]]
        res = 1
        while l < r < len(s):
            if l < r < len(s) and s[r] not in cur:
                cur.append(s[r])
                res = max(len(cur), res)
            else:
                while l < r < len(s) and s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                while l < r < len(s) and s[l] == s[r]:
                    l += 1
            r += 1
        return res
                            