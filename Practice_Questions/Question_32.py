"""
Using function write the code which tells number is even or odd
"""

def even_odd():
    num1 = int(input("Enter a Number: "))
    if num1 % 2 == 0:
        print(f"The Number {num1} is Even")
    else:
        print(f"The Number {num1} is Odd")

even_odd()