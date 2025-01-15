class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        s_d, t_d = defaultdict(int), defaultdict(int)
        for i in s:
            s_d[i] += 1
        for i in t:
            t_d[i] += 1

        if len(s_d) != len(t_d):
            return False

        for key, value in s_d.items():
            if key in t_d and value == t_d[key]:
                continue
            else:
                return False
        return True
