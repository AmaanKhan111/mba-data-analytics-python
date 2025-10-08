# # Lists in Python 
# # 1- Creating a list
# products = ["Laptop","Monitor","Tablet"]
# number = [10,20,30,40,50]
# mixed =["Revenue",2000,True,10.5]
# print(products)
# print(type(products))
# print(number)
# print(type(number))
# print(mixed)
# print(type(mixed))

# # 2- Indexing and slicing 
# sales = [100,200,300,400,500,600,700,800,900]
# print(sales[0]) # First element
# print(sales[4]) # Fifth element
# print(sales[-1]) # Last element
# print(sales[-3]) # Third last element
# print(sales[2:5]) # Slicing from index 2 to 4
# print(sales[:4]) # Slicing from start to index 3
# print(sales[5:]) # Slicing from index 5 to end
# print(sales[:]) # Slicing the entire list
# print(sales[::2]) # Slicing with step 2
# print(sales[::-1]) # Reversing the list

# # 3- updating and adding items 
# product = ["Laptop","Monitor","Tablet"]
# product[1]="Smartphone" # Updating the secound item
# product.append("Smartwatch") # Adding an item at the end
# product.extend(["Keyboard","Mouse"]) # Adding multiple items at the end
# product.insert(1,"Printer") # Adding an item at a specific index
# print(product)

# 4- Removing items
products = ["Laptop","Monitor","Tablet","Smartphone","smartwatch","keyboard","mouse"]
products.remove("Tablet") # Removing an item by value