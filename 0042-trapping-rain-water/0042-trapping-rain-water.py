class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        count = 0

        while left < right:
            if leftMax > rightMax:
                # move right
                right -= 1
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    count += rightMax - height[right]
            else:
                # move left
                left += 1
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    count += leftMax - height[left]
        return count