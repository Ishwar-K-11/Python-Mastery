try:
    num = int(input("Enter a Number : "))
    result = 100 / num

except ValueError:
    print("The ValueError Occurs")

except ZeroDivisionError:
    print("The ZeroDivisionError Occurs")

else:  # The else Block execuates only if the no exception occurs 
    print(f"The result is: {result}")

finally:  # The finally block gets always execuates
    print("Calulation Attempt complete")
