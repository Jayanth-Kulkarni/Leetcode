class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set_s, set_t = defaultdict(int), defaultdict(int)
        for i,j in zip(s,t):
            print(i,j)
            set_s[i] += 1
            set_t[j] += 1
        return set_s == set_t