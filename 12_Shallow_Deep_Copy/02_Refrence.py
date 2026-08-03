# Lets do Practical on refrence copy

list1 = [10, 20, 30, 40, 50]
print(list1)


list2 = list1  # Here you create a refrence copy of the list1 into list2
print(list2)

list2.append(100)  # You added 100 in the ending of the list2
print(list2)
print(list1)  # In the output you will see that in list1 the 100 also gets added


# So when we print the id of both list i will show same because:
# The equal(=) sign assigns only the id to another varible
# Its like same shirt having two or more tages


print(id(list1))
print(id(list2))
