Mar = {
    "Akshay" : [70, 80, 30, 60, 75],
    "Kartik" : [55, 65, 87, 85, 77],
    "Jack" : [97, 77, 55, 87, 66],
    "Ishu" : [98, 76, 79, 87, 77]
}

answ = dict(sorted(Mar.items(),key=lambda x: x[1][4]))
print(answ)

# Sorts the Dictionary according to the total value present in the list

"""
The following program gives the error - because the value present in the valuse are not full

Mar = {
    "Akshay" : [70, 80, 30, 60, 75],
    "Kartik" : [55, 65, 87, 88],
    "Jack" : [97, 77, 55],
    "Ishu" : [98, 76, 79, 87, 77]
}

answ = dict(sorted(Mar.items(),key=lambda x: x[1][4]))
print(answ)


"""


"""
Now suppose you have the same dictonary in which the list is not equal to each other but you want to sort it according to the sum in the list


Mar = {
    "Akshay" : [70, 80, 30, 60, 75],
    "Kartik" : [55, 65, 87],
    "Jack" : [97, 77, 55, 87, 66],
    "Ishu" : [98, 76, 79, 87, 77]
}

answ = dict(sorted(Mar.items(),key=lambda x: sum(x[1])))

answ = dict(sorted(Mar.items(),key=lambda x: sum(x[1]),reverse=True))
so it will print in the decending order

print(answ)

Now this works
"""

