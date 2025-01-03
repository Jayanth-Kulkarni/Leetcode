class Solution:
    from collections import Counter
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a,b = Counter(ransomNote), Counter(magazine)
        for i, j in a.items():
            if i in b and b[i] >= j:
                continue
            else:
                return False
        return True