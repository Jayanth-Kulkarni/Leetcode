class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        cur = defaultdict(int)
        l = 0
        for i in s1:
            target[i] += 1
        for r in range(len(s2)):
            cur[s2[r]] += 1
            if r-l+1 >= len(s1):
                if cur == target:
                    return True
                cur[s2[l]] -= 1
                if cur[s2[l]] == 0:
                    del cur[s2[l]]
                l += 1
        return False