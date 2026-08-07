"""# Here we will raise the exception in the code


def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be less then zero: ")

    elif age > 150:
        raise ValueError("Invalid Age")


check_age(160)
"""

# The above code gets work but there is one problem in that code is that it gets crash because:
# We have raise the exception manually we have't put it in the try and except block
# So now see the below code which works properly


def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be less then zero: ")

    elif age > 150:
        raise ValueError("Invalid Age")


try:
    check_age(160)
except ValueError as e:
    print(e)
