
# Ask user for revenue and cost.

 #Calculate and print profit and profit margin %

revenue = float(input("Enter revenue: "))
cost = float(input("Enter cost: "))

profit = revenue - cost
margin = (profit / revenue) * 100

print("Profit:", profit)
print("Profit Margin:", margin, "%")
