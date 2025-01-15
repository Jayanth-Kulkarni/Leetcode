class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s =="":
            return 0
        l, r = 0, 0
        cur = [s[r]]
        r += 1
        cur_max = 1
        while 0 <= l < r < len(s):
            if s[r] not in cur:
                cur.append(s[r])
                cur_max = max(cur_max, len(cur))
            else:
                while 0 <= l < r < len(s) and s[l] != s[r]:
                    cur.remove(s[l])
                    l += 1
                while 0 <= l < r < len(s) and s[l] == s[r]:
                    l += 1
            r += 1
        return cur_max