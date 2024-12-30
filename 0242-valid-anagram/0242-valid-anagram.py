class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i,j in zip(s,t):
            s_dict[i] += 1
            t_dict[j] += 1
        return s_dict == t_dict