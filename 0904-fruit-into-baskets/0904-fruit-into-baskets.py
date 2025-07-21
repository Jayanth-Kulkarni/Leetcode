class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        move from left to right and keep collecting, as soon as the dict > 3, start removing elements from left
        """
        l, r, res = 0, 0, 0
        d = defaultdict(int)
        while l <= r < len(fruits):
            d[fruits[r]] += 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res