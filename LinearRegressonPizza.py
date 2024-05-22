size = [6, 8, 12, 14, 18]
price = [350, 775, 1150, 1395, 1675]
new_size = int(input("Enter the size of the pizza: "))

# Calculate averages
xBar = sum(size) / len(size)
yBar = sum(price) / len(price)
xyBar = xyBar = (size[0] * price[0] + size[1] * price[1] + size[2] * price[2] + size[3] * price[3] + size[4] * price[4]) / len(size)
xQBar = sum(x ** 2 for x in size) / len(size)

# Calculate slope (m) and intercept (c)
m1 = (xBar * yBar) - xyBar
m2 = xBar ** 2 - xQBar
mFinal = m1 / m2
c = yBar - (mFinal * xBar)

# Calculate predicted price for the new size
y = (mFinal * new_size) + c
print("Price of %d inch Pizza is: %.2f" % (new_size, y))

# Calculate R-squared value
predicted_prices = [(mFinal * x) + c for x in size]
totalSumSQ = sum((y - yBar) ** 2 for y in price)
sumSQR = sum((y - y_pred) ** 2 for y, y_pred in zip(price, predicted_prices))
r_squared = (1 - (sumSQR / totalSumSQ)) * 100

print("R-squared value: %.2f" %r_squared)
