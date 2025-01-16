class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rd, md = defaultdict(int), defaultdict(int)
        for rn in ransomNote:
            rd[rn] += 1
        for rm in magazine:
            md[rm] += 1
        
        for i in rd:
            if i not in md or rd[i] > md[i]:
                return False
        return True