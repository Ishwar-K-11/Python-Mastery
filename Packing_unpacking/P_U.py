"""

Packing and unpacking is the very important concept in python

Lets Understand it through the Examples

"""

a = 1   # Considered as int
b = 1,  # Considered as Tuple

c,d = 10,20  # allowed in pthon so c= 10 and d=20


# Printing min and max of the tuple by using return 

def min_max(lst):
    mini = min(lst)
    maxi = max(lst)

    return mini, maxi

print(min_max([10,20,30,40]))
x,y = min_max([10,40,67,98,32])
print("Minimum Number: ",x)
print("Maximum Numver: ",y)
    