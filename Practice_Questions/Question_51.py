"""
In this code you have to replace the negative numvber with the zero
"""

def replace(lst):
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst

lst = [1,0,9,-2,-5,7,-4,99,-19,-84]
print(replace(lst))