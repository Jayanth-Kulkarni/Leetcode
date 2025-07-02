class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[0], height[right]
        count = 0
        while left < right:
            if leftMax > rightMax:
                # move right
                right -= 1
                rightMax = max(height[right], rightMax)
                if (min(leftMax,rightMax) - height[right]) > 0:
                    count += (min(leftMax,rightMax) - height[right])
            else:
                # move left
                left += 1
                leftMax = max(height[left], leftMax)
                if (min(leftMax,rightMax) - height[left]) > 0:
                    count += (min(leftMax,rightMax) - height[left])
        return count