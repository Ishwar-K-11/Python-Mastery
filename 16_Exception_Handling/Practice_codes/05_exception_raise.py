def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be less then zero: ")

    elif age > 150:
        raise ValueError("Invalid Age")

    print("The age is good")

try:
    check_age(160)

except ValueError as e:
    print(e)

except Exception as e:
    print(e)