class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        want, have, l = defaultdict(int), defaultdict(int), 0
        for chr in s1:
            want[chr] += 1
        for r in range(len(s2)):
            if r-l+1 > len(s1):
                have[s2[l]] -= 1
                if have[s2[l]] == 0:
                    del have[s2[l]]
                l += 1
            have[s2[r]] += 1
            if have == want:
                return True
        return False

