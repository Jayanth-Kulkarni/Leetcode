class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        window = set()
        l, r = 0, 0
        window.add(s[r])
        r += 1 
        max_length = 1
        while 0 <= l < r < len(s):
            if s[r] not in window:
                window.add(s[r])
                max_length = max(max_length, len(window))
            else:
                while l < r < len(s) and s[l] != s[r]:
                    window.remove(s[l])
                    l += 1
                while l < r < len(s) and s[l] == s[r]:
                    l += 1
            r += 1
        return max_length