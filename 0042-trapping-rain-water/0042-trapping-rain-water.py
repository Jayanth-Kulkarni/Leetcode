class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Find a min list and max list 
        """
        pre_max_list = [0]
        post_max_list = [0]
        result = 0
        for i in height:
            pre_max_list.append(max(i, pre_max_list[-1]))
        for i in height[::-1]:
            post_max_list.append(max(i, post_max_list[-1]))

        post_max_list = post_max_list[::-1]
        for i,j,k in zip(height,pre_max_list,post_max_list):
            if min(j,k) - i > 0:
                result += min(j,k) - i
        
        return result