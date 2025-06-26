"""
initialize left, right to 0 and lenght
If find area, compare with max and reset max if needed
if left is < right, move left pointer by 1 otherwise right by 1
Keep finding the max area while left < right
return max area
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_area = 0
        while left < right:
            max_area = max(max_area,(right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
