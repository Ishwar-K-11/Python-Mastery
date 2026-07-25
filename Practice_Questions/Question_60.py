"""
Given a list of numbers and you have the ask the user for the number. 
so the number which the users enters you have to remove all the occurences of that num from the list
"""

def duplicate(lst):
    while target in lst:
        lst.remove(target)
    print(lst)

target = int(input("Enter a target element: "))
lst = [1,1,6,7,9,6,5,4,4,5,8,2,8]
duplicate(lst)

# In this situation never run the for loop because it keeps at least one number which user have to remove