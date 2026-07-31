"""
1. strip()
-----------

    Definition:
        Removes leading (left) and trailing (right) whitespace or specified
        characters from a string.

    Syntax:
        string.strip([characters])

    Example:

        text = "   Python   "

        print(text.strip())

    Output:

        Python


2. lstrip()
------------

    Definition:
        Removes leading (left-side) whitespace or specified characters from a string.

    Syntax:
        string.lstrip([characters])

    Example:

        text = "   Python   "

        print(text.lstrip())

    Output:

        Python   


3. rstrip()
------------

    Definition:
        Removes trailing (right-side) whitespace or specified characters from a string.

    Syntax:
        string.rstrip([characters])

    Example:

        text = "   Python   "

        print(text.rstrip())

    Output:

        Python


Difference
----------

    strip()    -> Removes spaces from both left and right.

    lstrip()   -> Removes spaces only from the left.

    rstrip()   -> Removes spaces only from the right.
"""