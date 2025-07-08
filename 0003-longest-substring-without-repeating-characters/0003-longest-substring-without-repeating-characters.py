class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = max_count = 0
        current = set()
        while l <= r < len(s):
            while s[r] in current:
                current.remove(s[l])
                l += 1
            current.add(s[r])
            max_count = max(max_count, len(current))
            r += 1
        return max_count