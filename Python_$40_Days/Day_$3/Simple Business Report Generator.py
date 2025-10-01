#  Input: company name, revenue, cost.
#  Output: a formatted string report.

company = input("Enter Company Name: ")
revenue = float(input("Enter Revenue: "))
cost = float(input("Enter Cost: "))

profit = revenue - cost
margin = (profit / revenue) * 100

report = f"""
---- Business Report ----
Company: {company.strip().title()}
Revenue: ${revenue:,.2f}
Cost: ${cost:,.2f}
Profit: ${profit:,.2f}
Profit Margin: {margin:.2f}%
-------------------------
"""
print(report)
