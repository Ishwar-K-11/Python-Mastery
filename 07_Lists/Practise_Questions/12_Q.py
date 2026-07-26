"""
Using a list comprehension print the squares of odd numbers from 1 to 20

"""
squares = [i*i for i in range(1,21) if i % 2 != 0]
print(squares)