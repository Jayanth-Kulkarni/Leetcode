class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r = Counter(ransomNote)
        m = Counter(magazine)
        for char in r:
            if char in m and r[char] <= m[char]:
                continue
            else:
                return False
        return True 