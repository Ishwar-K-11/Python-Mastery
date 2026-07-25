# Given two list so you have to merge them in a single list without creating a new one

def rev(lst1,lst2):
    n = len(lst2)
    for i in range(0,n):
        lst1.append(lst2[i])

    return lst1

lst1 = [10,20,30,40,50]
lst2 = [50,60,70,80,20,80,77,98,98]

print("Before Merge: ",lst1)
rev(lst1,lst2)
print("List After Merge: ",lst1)

