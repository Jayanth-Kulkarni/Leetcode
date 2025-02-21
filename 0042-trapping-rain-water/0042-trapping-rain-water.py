class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [height[0]]
        rightmax = [height[-1]]
        for i in height[1:]:
            leftmax.append(max(leftmax[-1], i))
        height = height[::-1]
        for i in height[1:]:
            rightmax.append(max(rightmax[-1], i))
        rightmax, height = rightmax[::-1], height[::-1]
        res = 0
        for l, r, h in zip(leftmax, rightmax, height):
            if min(l,r) - h > 0:
                res += min(l,r) - h
        return res
