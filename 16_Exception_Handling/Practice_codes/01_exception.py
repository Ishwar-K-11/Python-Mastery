# This is our frist code of exception handling

try:
    num1 = int(input("Enter the frist number: "))
    num2 = int(input("Enter the second number: "))

    num3 = num1/num2
    print(f"{num1} Divides by {num2} we Get : {num3}")
    

except ZeroDivisionError:
    print("You cannot divide the number by zero")
