class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft, maxright, res = [height[0]], [height[-1]], 0
        for i in height[1:]:
            maxleft.append(max(maxleft[-1], i))
        rev = height[::-1]
        for i in rev[1:]:
            maxright.append(max(maxright[-1], i))
        maxright = maxright[::-1]
        for l, r, h in zip(maxleft, maxright, height):
            if (min(l,r) - h) > 0:
                res += min(l,r) - h
        return res
