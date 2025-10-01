# Day 3 – Strings in Python
# 🎯 Learning Goals

# Understand strings in Python.

# Learn indexing, slicing, and important methods.

# Apply strings in business data cleaning & reporting.

# 1 Strings Basics
# # Single, double, triple quotes
s1 = 'Business'
s2 = "Analytics"
s3 = """Data Analytics with Python"""

print(s1, s2, s3)


# ✅ Strings are immutable (cannot be changed directly).

# 2 Indexing & Slicing
text = "BusinessAnalytics"

# # Indexing
print(text[0])    # B (first char)
print(text[-1])   # s (last char)

# # Slicing
print(text[0:8])   # Business
print(text[8:])    # Analytics
print(text[:8])    # Business
print(text[0:15:2]) # Every 2nd char

# 3 String Methods (Very Important in Data Cleaning)
company = "   openAI Technologies   "

print(company.lower())    # lowercase
print(company.upper())    # uppercase
print(company.strip())    # remove spaces
print(company.replace("openAI", "Microsoft"))  

# # Searching
print(company.find("Tech"))    # returns index
print("AI" in company)         # True

# # Splitting & Joining
words = "Business,Finance,Analytics".split(",")
print(words)

joined = "-".join(words)
print(joined)   # Business-Finance-Analytics

# 4 String Formatting
# f-Strings (best for Business Reports)
revenue = 50000
profit = 12000
margin = (profit / revenue) * 100

report = f"Revenue: {revenue}, Profit: {profit}, Profit Margin: {margin:.2f}%"
print(report)

# 5 Small Business-Oriented Exercises

# Take a customer’s full name and print only the first name and last name separately.

# Write a program to check if a company name contains “Ltd” or “Inc”.

# Convert "product_sales_2025.csv" → "Product Sales 2025".

# Create an email ID using first name + last name (e.g., "John Doe" → "john.doe@company.com").

# Count how many times the word "profit" appears in a given report string.