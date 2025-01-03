class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        current = set()
        max_len = 0
        while l<=r and r<len(s):
            if s[r] not in current:
                current.add(s[r])
                max_len = max(len(current),max_len)
            else:
                while s[l] != s[r]:
                    current.remove(s[l])
                    l+=1
                while l<r and s[l] == s[r]:
                    l+=1
            r+=1
        return max_len
                
