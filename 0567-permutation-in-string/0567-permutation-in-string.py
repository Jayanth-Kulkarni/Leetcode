class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = defaultdict(int)
        current = defaultdict(int)
        l = r = 0
        for i in s1:
            check[i] += 1
        while l <= r < len(s2):
            if r-l < len(s1):
                current[s2[r]] += 1
                r += 1
            else:
                current[s2[l]] -= 1
                if current[s2[l]] == 0:
                    del current[s2[l]]
                l += 1
            if current == check:
                return True
        return False