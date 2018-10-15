hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# Iterate through the prices list and add each price to the variable total_price
for price in prices:
  total_price += price

# Calc average hairstyle price
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5
new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30. 
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)