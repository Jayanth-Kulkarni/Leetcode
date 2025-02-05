class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftmax, rightmax = [0], [0]
        for h in height:
            leftmax.append(max(leftmax[-1], h))
        for h in height[::-1]:
            rightmax.append(max(rightmax[-1], h))
        rightmax = rightmax[::-1]
        for l, r, h in zip(leftmax, rightmax, height):
            if min(l,r) - h > 0:
                res += min(l,r) - h
        return res