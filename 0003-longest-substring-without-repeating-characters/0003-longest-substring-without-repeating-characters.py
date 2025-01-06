class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # using sliding window approach
        # l = 0, r = len(s) - 1 loop through the string
        # if ele not in current add it to current
        # if ele in current, while l not= ele -> l+=1 otherwise remove from current and l += 1
        if len(s) == 0:
            return 0
        l, r = 0, 1
        current = set()
        current.add(s[0])
        max_len = len(current)
        while l < r < len(s):
            if s[r] not in current:
                current.add(s[r])
                max_len = max(max_len, len(current))
            else:
                while l < r < len(s) and s[l] != s[r]:
                    current.remove(s[l])
                    l += 1
                while l < r < len(s) and s[l] == s[r]:
                    l += 1
            r+=1
        return max_len
