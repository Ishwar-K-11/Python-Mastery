"""
CASE CONVERSION
    1) upper() : Converts all characters of the string to uppercase
    2) lower() : Converts all characters of the string to lowercase
    3) title() : Converts the frist character of each words in the string to uppercse and remaning characters of the word to lowercase
    4) capitalize() : Convert drist character of the entire string to uppercase and remaning to lowercase
    5) swapcase() : Swap the case of each characters - uppercase to lowercase and lowercase to uppercase 

"""

string = "Python Program are easy to unDersTanD 10 {} :: 1020"
print(f"Uppercase : {string.upper()}")
print(f"Lowercase : {string.lower()}")
print(f"Title : {string.title()}")
print(f"Capitalize : {string.capitalize()}")
print(f"SwapCase : {string.swapcase()}")

# Keep in mind that string is immutable so it does not affest the original string or you cannot change original one
