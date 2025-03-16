class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds, dt = defaultdict(int), defaultdict(int)
        for i in s:
            ds[i] += 1
        for i in t:
            dt[i] += 1
        
        return ds == dt