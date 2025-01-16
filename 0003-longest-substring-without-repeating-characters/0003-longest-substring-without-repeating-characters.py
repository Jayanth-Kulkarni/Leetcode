class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        window = [s[r]]
        r+=1
        res = 1
        while 0 <= l < r < len(s):
            if s[r] not in window:
                window.append(s[r])
                res = max(res, len(window))
            else:
                while 0 <= l < r < len(s) and s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                while 0 <= l < r < len(s) and s[l] == s[r]:
                    l += 1
            r += 1
        return res