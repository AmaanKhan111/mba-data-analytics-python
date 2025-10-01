
# Ask user for revenue and cost.

 #Calculate and print profit and profit margin %

revenue = float(input("Please Enter revenue: "))
cost = float(input("Please Enter cost: "))

profit = revenue - cost
margin = (profit/revenue) * 100

print("Profit:", profit)
print("Profit Margin:", margin,"%")
