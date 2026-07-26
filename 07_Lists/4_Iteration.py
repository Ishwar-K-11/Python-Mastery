"""
Iterating or Looping allows you to process each items peform calculations or display contents
Python allow you to this using the for and while loop
"""

"""
Using For loop
fruits = ["Apple", "Mango", "Watermelon", "Banana"]
for fruit in fruits:
    print(fruit)
"""

"""
Using While loop
fruits = ["Apple", "Mango", "Watermelon", "Banana"]
i = 0
while i < len(fruits)
    print(fruits[i])
    i += 1
"""

# Examples 
Num = [1,4,5,7,9,8,3,89,76,45]

#While loop
i = 0
n = len(Num)
while i <= n-1:
    print(Num[i],end=" ")
    i+=1

total = 0
i = 0
n = len(Num)
while i <= n-1:
    if Num[i] % 2 == 0:
        total += 1
    i+=1
print("\nTotal Even Nymbers In List are: ",total)



# For Loop
#total of number
total_of_number = 0
for i in range(0, n):
    print(Num[i], end=" ")
    total_of_number += Num[i]

print("\nTotal Of List: ",total_of_number)


# Easy one
total2 = 0
for nums in Num:
    total2 += nums
print("total", total2)

#Iterating in Reverse manner
for nums in Num[::-1]:
    print(nums,end=" ")




