"""
Membership Operators

Membership operators are used to check whether a value exists in a sequence such as a list, tuple, string, set, or dictionary. They return a Boolean value (`True` or `False`).

1] in
    Checks if the specified value is present in the sequence.
    Returns True if the value exists; otherwise, returns False.

    fruits = ["apple", "banana", "orange"]
    print("banana" in fruits)   #Output True
    print("grapes" in fruits)   #Output False

2] not in
    Checks if the specified value is not present in the sequence.
    Returns True if the value does not exist; otherwise, returns False.

    fruits = ["apple", "banana", "orange"]
    print("grapes" not in fruits)   #Output True
    print("banana" not in fruits)   #Output False
"""