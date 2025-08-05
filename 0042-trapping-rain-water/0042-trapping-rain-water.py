class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax = [height[0]], [height[-1]]
        res = 0
        for h in height[1:]:
            leftmax.append(max(h, leftmax[-1]))
        for h in reversed(height):
            rightmax.append(max(h, rightmax[-1]))
        rightmax.pop(0)
        rightmax = rightmax[::-1]
        for i in range(len(height)):
            if min(leftmax[i],rightmax[i]) - height[i] > 0:
                res += min(leftmax[i],rightmax[i]) - height[i]
        return res