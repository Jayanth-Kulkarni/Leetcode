class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        res, l  = 0, 0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            res = max(res, len(char))
        return res