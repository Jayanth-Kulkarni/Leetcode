# prices = [7,1,5,3,6,4]
prices = [7, 6, 4, 3, 1]
lowest = prices[0]
maxProfit = 0
for price in prices:
    if lowest > price:
        lowest = price
    elif price - lowest > maxProfit:
        maxProfit = price - lowest

print(maxProfit)