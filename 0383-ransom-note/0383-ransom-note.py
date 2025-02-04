class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rd, md = defaultdict(int), defaultdict(int)
        for rn in ransomNote:
            rd[rn] += 1
        for mn in magazine:
            md[mn] += 1
        
        for rn in ransomNote:
            if rn not in md or (rn in md and md[rn] < rd[rn]):
                return False
        return True