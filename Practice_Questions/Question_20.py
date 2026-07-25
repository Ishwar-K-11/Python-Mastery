"""
take the numbers from the user until the user enters a negative number and print the sum 
of all the numbers entered by the user.

"""
total = 0
while True:
    num = int(input("Enter a Number: "))
    if num < 0:
        continue
    if num == 0:
        break
    total += num

print("The total sum of all the numbers entered is:", total)

    