import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))


from calculator import add

print(add(20, 10))


import calculator as calc

print(calc.add(30, 20))


from calculator import add, subtract

print(add(50, 10))
print(subtract(50, 10))