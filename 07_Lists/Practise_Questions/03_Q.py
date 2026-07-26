"""
Ask user to enter the list numbers and print the avg of it without using the build in avg function 

"""

l_ist = list(map(int,input("Enter the list numbers(Space Seperated)").split()))
total = 0
n = len(l_ist)
for nums in l_ist:
    total += nums

avg = total / n
print("The Average of list is :", avg)