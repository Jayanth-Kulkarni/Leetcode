class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        left, right = 0, len(height)-1
        leftMax, rightMax = height[left], height[right]
        while left < right:
            if leftMax > rightMax:
                # move right by 1
                right -= 1
                rightMax = max(rightMax, height[right])
                if min(leftMax, rightMax) - height[right] > 0:
                    count +=  min(leftMax, rightMax) - height[right]
            else:
                # move left by 1
                left += 1
                leftMax = max(leftMax, height[left])
                if min(leftMax, rightMax) - height[left] > 0:
                    count += min(leftMax, rightMax) - height[left]
        
        return count