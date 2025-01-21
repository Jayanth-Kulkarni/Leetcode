class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rd, md = defaultdict(int), defaultdict(int)
        for rn in ransomNote:
            rd[rn] += 1
        for mn in magazine:
            md[mn] += 1
        for n in rd:
            if n in md and md[n] >= rd[n]:
                continue
            return False
        return True
