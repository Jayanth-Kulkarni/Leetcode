# height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
height = [2, 3, 10, 5, 7, 8, 9]
area = -1
cur_area = -1
left_flag = False
left, right = 0, len(height) - 1
while left < right:
    print(left, right, cur_area, left_flag)
    cur_area = (right - left) * min(height[left], height[right])
    if cur_area > area:
        area = cur_area
    elif left_flag != True:
        left += 1
        left_flag = True
    elif left_flag:
        right -= 1
        left_flag = False
print(area)