# Take three Number as input. Print the largest of the three without using any build in function.

num1, num2, num3 = map(int, input("Enter 3 Numbers(separated by space): ").split())

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is: {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is: {num2}")
else:
    print(f"The largest number is: {num3}")