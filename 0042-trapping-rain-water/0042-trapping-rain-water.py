class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax, rightmax = [height[0]], [height[-1]]
        for h in height:
            leftmax.append(max(leftmax[-1], h))
        for h in range(len(height)-1,-1,-1):
            rightmax.append(max(rightmax[-1],height[h]))
        rightmax = rightmax[::-1]
        res = 0
        for i in range(len(height)):
            if min(leftmax[i], rightmax[i]) - height[i] > 0:
                res += min(leftmax[i], rightmax[i]) - height[i]
        return res