class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_dict = defaultdict(int)
        current_dict = defaultdict(int)
        for i in s1:
            target_dict[i] += 1
        l = 0
        for r in range(len(s2)):
            current_dict[s2[r]] += 1
            if r-l+1 == len(s1):
                if current_dict == target_dict:
                    return True
                current_dict[s2[l]] -= 1
                if current_dict[s2[l]] == 0:
                    del current_dict[s2[l]]
                l+=1
        
        return False