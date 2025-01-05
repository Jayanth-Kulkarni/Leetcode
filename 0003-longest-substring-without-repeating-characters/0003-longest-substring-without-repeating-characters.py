class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length = 0
        current = set()
        while l <= r < len(s):
            if s[r] not in current:
                current.add(s[r])
                max_length = max(max_length, len(current))
            else:
                while l < r and s[l] != s[r]:
                    current.remove(s[l])
                    l += 1
                while l < r and s[l] == s[r]:
                    l += 1
            r+=1
        return max_length