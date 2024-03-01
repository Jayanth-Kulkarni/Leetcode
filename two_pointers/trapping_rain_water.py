def rain_water(heights):
    maxLeft,maxRight = [0], [0]
    maxLeft_val = -1
    maxRight_val = -1
    for idx,i in enumerate(heights[1:]):
        maxLeft_val = max(heights[idx],maxLeft_val)
        maxLeft.append(maxLeft_val)
    reversed_height = heights[::-1]
    for idx,i in enumerate(reversed_height[1:]):
        maxRight_val = max(reversed_height[idx],maxRight_val)
        maxRight.append(maxRight_val)
    maxRight = maxRight[::-1]
    trap = []
    for idx,i in enumerate(heights):
        trap.append(min(maxLeft[idx],maxRight[idx])-i)
    sum = 0
    for i in trap:
        if i>0:
            sum+=i
    return sum