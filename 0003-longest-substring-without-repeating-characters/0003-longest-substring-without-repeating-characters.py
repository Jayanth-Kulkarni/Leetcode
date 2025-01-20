class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0 
        cur = []
        left, right = 0, 0
        cur.append(s[right])
        max_len = 1
        right += 1
        while 0 <= left < right < len(s):
            if s[right] not in cur:
                cur.append(s[right])
                max_len = max(max_len, len(cur))
            else:
                while 0 <= left < right < len(s) and s[left] != s[right]:
                    cur.remove(s[left])
                    left += 1
                while 0 <= left < right < len(s) and s[left] == s[right]:
                    left += 1
            right += 1
        
        return max_len