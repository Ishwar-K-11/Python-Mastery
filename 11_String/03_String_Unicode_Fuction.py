"""
ord() Function
--------------

The ord() function is a built-in Python function that returns the
Unicode value (integer value) of a single character.

Syntax
------

ord(character)

Example
-------

print(ord("A"))
print(ord("a"))

Output
------

65
97

Explanation
-----------

• The character 'A' has a Unicode (ASCII) value of 65.
• The character 'a' has a Unicode (ASCII) value of 97.

Since uppercase and lowercase letters have different Unicode values,
their output is different.

Some Common Unicode Values
--------------------------

'A' -> 65
'B' -> 66
'Z' -> 90

'a' -> 97
'b' -> 98
'z' -> 122

'0' -> 48
'9' -> 57

' ' (Space) -> 32

Uses of ord()
-------------

• Convert a character into its Unicode value.
• Compare characters.
• Check whether a character is uppercase or lowercase.
• Encryption and text processing.

Reverse Function
----------------

The opposite of ord() is chr().

Example:

print(chr(65))
print(chr(97))

Output:

A
a

Note
----

• ord() accepts only one character.
• Passing more than one character will produce a TypeError.

Example:

print(ord("AB"))

Output:

TypeError: ord() expected a character, but string of length 2 found


"""


print(ord("M"))
print(chr(98))


# The main use of Unicode Function is for methods like min() and max on the string
string = "Python Programming"
print(min(string))   # min() returns the character with the smallest Unicode value. And the smallest value is ' '(space) = 32 
print(max(string))
print(sorted(string))
