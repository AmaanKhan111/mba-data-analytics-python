# Input: revenue, cost, tax rate.

# Output:

# Profit before tax

# Tax amount

# Net profit

# Profit margin %
revenue = float(input("Enter Revenue: "))
cost = float(input("Enter Cost: "))
tax_rate = float(input("Enter Tax Rate (%): "))

profit_before_tax = revenue - cost
tax = (profit_before_tax * tax_rate) / 100
net_profit = profit_before_tax - tax
margin = (net_profit / revenue) * 100

print("Profit Before Tax:", profit_before_tax)
print("Tax Amount:", tax)
print("Net Profit:", net_profit)
print("Profit Margin %:", margin)



