class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = defaultdict(int)
        window_dict = defaultdict(int)
        for idx, i in enumerate(s1):
            target[i] += 1
            window_dict[s2[idx]] += 1
        l = 0
        if target == window_dict:
            return True
        for r in range(len(s1), len(s2)):
            window_dict[s2[r]] += 1
            window_dict[s2[l]] -= 1
            if window_dict[s2[l]] == 0:
                del window_dict[s2[l]]
            if target == window_dict:
                return True
            l += 1
        return False