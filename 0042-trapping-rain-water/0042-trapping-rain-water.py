class Solution:
    def trap(self, height: List[int]) -> int:
        premax = [0]
        postmax = [0]
        for i in height:
            premax.append(max(premax[-1], i))
        
        for i in height[::-1]:
            postmax.append(max(postmax[-1], i))
        
        postmax = postmax[::-1]
        print(premax, postmax)
        res = 0
        for i, j, h in zip(premax, postmax, height):
            if min(i,j) - h > 0:
                res += min(i,j) - h
        
        return res