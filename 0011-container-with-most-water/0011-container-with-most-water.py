class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxArea = 0
        while left < right:
            area = min(height[left], height[right]) * (right-left)
            maxArea = max(maxArea, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea