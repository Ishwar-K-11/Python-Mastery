"""
write a program that takes a list and a target number. Use a loop to determine if the target number exists in the list. Do not use the operator
"""

my_list = list(map(int,input("Enter the Numbers to get store in the List (Space Seperated): ").split()))

# You can cover into list like  lst = my_list  ## Not like lst =[my_list]

target = int(input("Enter the target number to print its position: "))
n = len(my_list)
for i in range(n):
    if my_list[i] == target:
        print("The position is: ",i+1)

        found = True
        break

if not found:
    print("Element not found")