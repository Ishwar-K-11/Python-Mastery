"""
Element wise the sum of two list
Given a two lists of the same lenght. wirte a python code using a loop to create
a new list where each element in the sum of corresponding both original list
"""

list1 = list(map(int,input("Enter the list numbers(Space Seperated): ").split()))
list2 = list(map(int,input("Enter the list numbers(Space Seperated): ").split()))

sum_list = []
for i in range(len(list1)):
    sum_list.append(list1[i]+list2[i])

print("The Sum of List: ",sum_list)