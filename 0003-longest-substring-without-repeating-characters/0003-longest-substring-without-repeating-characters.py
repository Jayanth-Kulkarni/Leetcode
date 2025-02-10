class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l, r = 0, 1
        window = [s[0]]
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