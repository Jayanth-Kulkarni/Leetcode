class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count_ransom, count_magazine = Counter(ransomNote), Counter(magazine)
        for value, count in count_ransom.items():
            if value not in count_magazine or count_magazine[value] < count:
                return False
        return True