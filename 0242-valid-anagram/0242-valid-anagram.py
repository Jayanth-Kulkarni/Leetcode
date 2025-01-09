class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        c_s = defaultdict(int)
        c_t = defaultdict(int)

        
        for i,j in zip(s,t):
            c_s[i] += 1
            c_t[j] += 1
        
        return c_s == c_t