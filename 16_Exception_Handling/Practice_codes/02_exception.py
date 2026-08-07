# Here we will try to execuate the exceptions using the function

try:

    def Division(num1: int, num2: int):
        return num1 / num2

    Division("abc", 8)

except ZeroDivisionError:
    print("ZeroDivisionError Occurs")

except TypeError:
    print("The TypeError Occurs")
