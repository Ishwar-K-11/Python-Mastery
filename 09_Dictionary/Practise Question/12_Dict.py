"""
Q Create two dictionary dic1 and dic2 which contains product and price or anything you want 
    1. Combine two dictionary or merge them 
    2. use the update method
    3. do not harm the dic1

"""

dic1 = {
    "Milk" : 30,
    "Eggs" : 70,
    "Maggi" : 20,
    "Ghee" : 700
}

dic2 = {
    "Notebook" : 100,
    "Pencil" : 7,
    "Bottle" : 231
}

for items, price in dic2.items():
    dic1.update({items : price})

print(dic1)



# Execuating the same code using function 
"""
def merge_dictionary(dic1, dic2):
    new_dict = dic1.copy()      # Keeps dic1 unchanged

    for item, price in dic2.items():
        new_dict.update({item: price})

    return new_dict


dic1 = {
    "Milk": 30,
    "Eggs": 70,
    "Maggi": 20,
    "Ghee": 700
}

dic2 = {
    "Notebook": 100,
    "Pencil": 7,
    "Bottle": 231
}

merged = merge_dictionary(dic1, dic2)

print("Dictionary 1:", dic1)
print("Dictionary 2:", dic2)
print("Merged Dictionary:", merged)
"""

