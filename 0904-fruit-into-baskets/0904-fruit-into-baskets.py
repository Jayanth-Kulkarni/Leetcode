class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = r = max_count = 0
        count = defaultdict(int)
        while l <= r < len(fruits):
            count[fruits[r]] += 1
            while l <= r < len(fruits) and len(count) > 2:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1    
            
            max_count = max(max_count, r - l + 1)
            r += 1
        return max_count