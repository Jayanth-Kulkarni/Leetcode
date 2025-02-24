class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxarea = 0
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r])*(r-l))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        return maxarea