class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        max_left, max_right = [height[0]], [height[-1]]
        for i in height[1:]:
            max_left.append(max(i,max_left[-1]))
        height = height[::-1]
        for i in height[1:]:
            max_right.append(max(i,max_right[-1]))
        max_right = max_right[::-1]
        for i in range(len(max_left)):
            res += min(max_right[i], max_left[i]) - height[i]
        return res