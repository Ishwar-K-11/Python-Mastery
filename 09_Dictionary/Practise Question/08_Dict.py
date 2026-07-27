"""
Product Price Lookup
    Construct a dictionary for product names and their price.
    Prompt the user to enter the product name. use the in keyword to check if it is exists
    if exits display the price and if not print product not dound

"""

Products = {
    "Milk" : 30,
    "Bread" : 60,
    "Eggs" : 70,
    "Oats" : 300,
    "Banana" : 60,
}

product = input("Enter The Name of Product :")

if product in Products:
    print(f"Product : {product}")
    print(f"Price : {Products[product]}")
else:
    print("Product Not Found")
