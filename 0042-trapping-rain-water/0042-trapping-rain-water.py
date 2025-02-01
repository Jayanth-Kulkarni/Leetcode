class Solution:
    def trap(self, height: List[int]) -> int:
        # find the min from left 
        # find the min from right
        minLeft, minRight = [0], [0]
        for i in height:
            minLeft.append(max(minLeft[-1], i))
        
        for i in height[::-1]:
            minRight.append(max(minRight[-1], i))

        minRight = minRight[::-1]

        res_val = 0
        for l, r, h in zip(minLeft, minRight, height):
            if min(l, r) - h  > 0:
                res_val += min(l, r) - h
        
        return res_val