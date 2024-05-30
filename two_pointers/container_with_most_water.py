# # height = [1,8,6,2,5,4,8,3,7]
# # height = [1,1]
# height = [2, 3, 10, 5, 7, 8, 9]
# area = -1
# cur_area = -1
# left_flag = False
# left, right = 0, len(height) - 1
# while left < right:
#     print(left, right, cur_area, left_flag)
#     cur_area = (right - left) * min(height[left], height[right])
#     if cur_area > area:
#         area = cur_area
#     elif left_flag != True:
#         left += 1
#         left_flag = True
#     elif left_flag:
#         right -= 1
#         left_flag = False
# print(area)


def container_with_most_water(height):
    left,right = 0,len(height)-1
    biggest_area = -1
    right_flag = False
    while left<right:
        cur_area = min(height[left], height[right]) * (right-left)
        if height[left]>height[right]:
            right_flag=True
        else:
            right_flag=False
        if cur_area>biggest_area:
            biggest_area = cur_area
        elif right_flag:
            right -= 1
        else:
            left += 1
    return biggest_area

# height = [7, 7, 2]
# print(container_with_most_water(height))


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maxHeight = 0
        while l<r:
            currentHeight = min(height[l],height[r]) * (r-l)
            maxHeight = max(maxHeight,currentHeight)
            if height[l]<height[r] and l<r:
                l+=1
            elif l<r:
                r-=1
        return maxHeight