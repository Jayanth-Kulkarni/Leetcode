class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = res = 0
        ch_set = set()
        for r in range(len(s)):
            while s[r] in ch_set:
                ch_set.remove(s[l])
                l += 1
            ch_set.add(s[r])
            res = max(res, len(ch_set))
        return res 