"""
Print all the factors of a number
"""

def Prime():
    num = int(input("Enter a Number: "))
    for i in range(1,num+1):
        if num % i == 0:
            print(i,end="  ")


Prime()
