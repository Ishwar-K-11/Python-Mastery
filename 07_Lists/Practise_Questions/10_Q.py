"""
Create a list contaning the square of numbers from the 0 to 100
"""

def square_num():
    sq_num = []
    for i in range(1,101):
        sq_num.append(i*i)
    print("Squre of Numbers from 1 to 100: ",sq_num)

square_num()