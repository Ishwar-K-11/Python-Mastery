# Take a number as input and using the turnary operator print weather that nnumver is even or odd.


num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")