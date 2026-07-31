"""
1. count()
-----------

    Definition:
        Returns the number of times a specified character or substring appears in a string.

    Syntax:
        string.count(value)

    Example:

        text = "Python Programming"

        print(text.count("m"))
        print(text.count("o"))

    Output:

        2
        2


2. find()
----------

    Definition:
        Returns the index of the first occurrence of a specified character or substring.
        Returns -1 if the value is not found.

    Syntax:
        string.find(value)

    Example:

        text = "Python Programming"

        print(text.find("P"))
        print(text.find("o"))
        print(text.find("Java"))

    Output:

        0
        4
        -1


3. index()
-----------

    Definition:
        Returns the index of the first occurrence of a specified character or substring.
        Raises a ValueError if the value is not found.

    Syntax:
        string.index(value)

    Example:

        text = "Python Programming"

        print(text.index("P"))
        print(text.index("o"))

    Output:

        0
        4


4. replace()
-------------

    Definition:
        Replaces all occurrences of a specified substring with another substring.

    Syntax:
        string.replace(old, new)

    Example:

        text = "Python Programming"

        print(text.replace("Python", "Java"))

    Output:

Java Programming
"""

text = "Python is a good programming language"
print(text.count("good"))
print(text.find("Java"))
print(text.index("l"))
print(text.replace("Python", "Java"))



phone = "+91988-898-9876"
# Remove dashes and country code

clean = phone.replace("-","").replace("+91","")
print(clean)
