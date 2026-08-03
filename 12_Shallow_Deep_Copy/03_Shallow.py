# The shallow copy creates a new actual outer object

list_1 = [10, 20, 30, 40, 50]


import copy

list_2 = copy.copy(list_1)

print(list_1)
print(list_2)

print(id(list_1))
print(id(list_2))


list_2.append(100)
print(list_2)
print(
    list_1
)  # Here you can see that the element 100 not get added to the original list


# There is one problem with the shallow copy
# The problem is the nested object are shared between the original

# Example:
list_5 = [10, 30, [100, 150, 200], 50, 70]
# So indexing Becomes  0   1      0    1    2     3   4

list_6 = copy.copy(list_5)
list_6.append(500)
print(list_6)
print(
    list_5
)  # So here ou can see that number 500 got added in the list_6 which is shallow copy of the list_5


# The actual problem is here when you update the element of the innder(nested) list the original list alos get changes
list_6[2][2] = 999
print(list_6)
print(
    list_5
)  # Here you can see that the number 999 gets added to the original list because you have use shallow copy
