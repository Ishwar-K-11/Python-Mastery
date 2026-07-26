"""
Create a Function Add which takes two arguments and add them and print
"""

def Add(a,b):
    print(f"The sum of Number {a} and {b} is {a+b}")
num1, num2 = map(int,input("Enter Two Numbers(Space seperated) : ").split())
Add(num1,num2)