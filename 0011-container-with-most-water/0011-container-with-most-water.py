class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_height = 0
        while l<r:
            max_height = max(max_height, (r-l)*min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_height
                