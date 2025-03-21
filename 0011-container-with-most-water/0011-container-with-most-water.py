class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxarea = 0
        for i in range(len(height)):
            maxarea = max(maxarea, min(height[left], height[right])* (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxarea