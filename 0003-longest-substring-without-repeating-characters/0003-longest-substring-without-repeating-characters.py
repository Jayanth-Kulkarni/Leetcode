class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        move right pointer by 1 and see if it is not in the set, add it and increment the res count
        If we see a letter repeat, starting from the left pointer keep moving right by 1 and delete the element in the set and decrement current length, repeat until end of string
        """
        l, r = 0, 0
        cur = set()
        res = 0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l+=1
            cur.add(s[r])
            res = max(res,len(cur))
        return res
                