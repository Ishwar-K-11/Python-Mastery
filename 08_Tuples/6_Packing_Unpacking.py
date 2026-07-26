"""
1] Tuple Packing

   Storing multiple values together in a tuple is called
   tuple packing.

   Example:

   student = ("Ishwar", 20, 8.5)

   Parentheses are optional while packing:

   student = "Ishwar", 20, 8.5


============================================================
2] Tuple Unpacking

   Extracting tuple elements into separate variables is
   called tuple unpacking.

   Example:

   student = ("Ishwar", 20, 8.5)

   name, age, cgpa = student


   Using * while unpacking:

   tup = (10, 20, 30, 40, 50)

   a, *b, c = tup

   a -> 10
   b -> [20, 30, 40]
   c -> 50

   Note:
   Values collected using * are stored in a list.


============================================================
3] Joining Tuples

   The + operator is used to join two tuples.

   Example:

   tup1 = (1, 2, 3)
   tup2 = (4, 5, 6)

   tup3 = tup1 + tup2

   Result:
   (1, 2, 3, 4, 5, 6)


============================================================
4] Repeating Tuple Elements

   The * operator is used to repeat a tuple.

   Example:

   tup = (1, 2)

   tup * 3

   Result:
   (1, 2, 1, 2, 1, 2)


============================================================
5] Nested Tuple

   A tuple can contain another tuple.

   Example:

   matrix = (
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9)
   )

   matrix[0]     -> (1, 2, 3)
   matrix[1][2]  -> 6


============================================================
6] Converting List to Tuple

   tuple() is used to convert a list into a tuple.

   lst = [10, 20, 30]

   tup = tuple(lst)

   Result:
   (10, 20, 30)


============================================================
7] Converting Tuple to List

   list() is used to convert a tuple into a list.

   tup = (10, 20, 30)

   lst = list(tup)

   Result:
   [10, 20, 30]


============================================================
8] Modifying a Tuple

   A tuple cannot be modified directly because it is
   immutable.

   To modify its values:

   Tuple -> List -> Modify -> Tuple

   Example:

   tup = (10, 20, 30)

   lst = list(tup)
   lst[1] = 100
   tup = tuple(lst)

   Result:
   (10, 100, 30)


============================================================
9] Deleting a Tuple

   Individual elements cannot be deleted from a tuple.

   The entire tuple can be deleted using del.

   Example:

   tup = (10, 20, 30)

   del tup


============================================================
10] Tuple Operators

   +       -> Concatenation
   *       -> Repetition
   in      -> Checks if value exists
   not in  -> Checks if value does not exist
"""