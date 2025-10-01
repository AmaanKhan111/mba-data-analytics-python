# 📅 Day 2 – Python Operators & Expressions
# 🎯 Learning Goals

# Understand and practice Python operators.

# Learn how expressions are formed.

# Apply operators in business-related mini problems.

# 1 Python Operators
# Arithmetic Operators
a = 15
b = 4

print("Addition:", a + b)      # 19
print("Subtraction:", a - b)   # 11
print("Multiplication:", a * b) # 60
print("Division:", a / b)      # 3.75
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)       # 3
print("Exponent:", a ** b)     # 15^4 = 50625

# Comparison Operators
x = 20
y = 10

print(x > y)   # True
print(x < y)   # False
print(x == y)  # False
print(x != y)  # True

# Logical Operators
is_analytics = True
is_finance = False

print(is_analytics and is_finance)  # False
print(is_analytics or is_finance)   # True
print(not is_analytics)             # False

# Assignment Operators
revenue = 1000
revenue += 500   # same as revenue = revenue + 500
print(revenue)   # 1500

# Bitwise Operators (optional for data analytics, but useful to know)
a = 5   # 101 in binary
b = 3   # 011 in binary

print(a & b)  # AND → 1
print(a | b)  # OR → 7
print(a ^ b)  # XOR → 6

# 2 Expressions

# 👉 Expressions combine variables, values, and operators.

profit = 1200
revenue = 5000

profit_margin = (profit / revenue) * 100
print("Profit Margin:", profit_margin, "%")

#  Small Business-Oriented Exercises

# Write a program that calculates the ROI given profit and investment.
# Formula: ROI = (Profit / Investment) * 100.

# Check if a company is profitable or not (profit > 0).

# Calculate the Net Profit: Revenue - (COGS + Operating Expenses + Taxes).

# Write a program to check if a year is leap year (using % operator).