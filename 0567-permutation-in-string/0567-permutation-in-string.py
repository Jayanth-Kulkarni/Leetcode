class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        valid, cur = defaultdict(int), defaultdict(int)
        for i in s1:
            valid[i] += 1
        for r in range(len(s2)):
            cur[s2[r]] += 1
            if r-l+1 > len(s1):
                cur[s2[l]] -=1
                if cur[s2[l]] == 0:
                    del cur[s2[l]]
                l += 1
            if cur == valid:
                return True
        return False