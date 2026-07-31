"""
Checking content in the string with build in methods
"""

string1 = "programming language"
string2 = "      "
string3 = "123456"
string4 = "pythonlanguage1234"

print(string1.isalpha())  # Checks all the string is alphabetic and no empty
print(string3.isdigit())  # Checks is string contains only the digits
print(string4.isalnum())  # Checks is the string is alphanumeric only
print(string2.isspace())  # Checks all the string is white space
print()
print()


# Checking prefix and suffix
print(string1.endswith("age"))
print(string1.endswith(".pdf"))
print(string1.startswith("pro"))


# Simple use case
# when you ask a user for age and by accidently he enters the name so the program get crash for precaution you can use isdigit()
age = input("Enter your age : ")
if age.isdigit():
    if int(age) >= 18:
        print("Eligable")
    else:
        print("Not Eligable")
else:
    print("Enter The Age in numbers")
