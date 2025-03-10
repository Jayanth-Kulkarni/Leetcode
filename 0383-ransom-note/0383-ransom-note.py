class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rd = defaultdict(int)
        md = defaultdict(int)
        for r in ransomNote:
            rd[r] += 1
        for m in magazine:
            md[m] += 1
        
        for i in rd:
            if i not in md:
                return False
            if i in md and md[i] < rd[i]:
                return False
        return True

