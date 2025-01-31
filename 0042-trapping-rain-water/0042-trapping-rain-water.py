class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0], [0]
        for h in height:
            maxLeft.append(max(h, maxLeft[-1]))
        for h in height[::-1]:
            maxRight.append(max(h, maxRight[-1]))
        maxRight = maxRight[::-1]
        res = []
        for l, r, h in zip(maxLeft, maxRight, height):
            res.append(min(l, r) - h)
        ans = 0
        for r in res:
            if r>0:
                ans+=r  
        return ans