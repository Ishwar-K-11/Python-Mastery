"""
1] What is a Tuple?

   A tuple is a collection used to store multiple values
   in a single variable.

   Tuples are written using parentheses ().

   Example:
   tup = (10, 20, 30, 40)



2] Characteristics of Tuple

   1) Ordered
      Elements maintain their order and position.

   2) Immutable
      Once a tuple is created, its elements cannot be
      changed, added, or removed.

   3) Allows Duplicate Values
      A tuple can contain the same value multiple times.
      Example: (10, 20, 10, 30)

   4) Allows Different Data Types
      A tuple can contain int, float, string, boolean, etc.
      Example: (10, "Python", 3.14, True)

   5) Indexed
      Each element has an index starting from 0.

   6) Supports Negative Indexing
      Negative indexing starts from the last element.
      -1 represents the last element.

   7) Supports Slicing
      A portion of a tuple can be accessed using slicing.

   8) Allows Nested Collections
      A tuple can contain lists, tuples and other collections.



3] Creating Tuples

   Empty Tuple:
   tup = ()

   Multiple Elements:
   tup = (10, 20, 30)

   Different Data Types:
   tup = (10, "Hello", 3.14, True)

   Single Element Tuple:
   tup = (10,)

   Note:
   A comma is required for a single-element tuple.

   (10,)  -> Tuple
   (10)   -> Integer



4] Accessing Tuple Elements

   Tuple elements are accessed using indexes.

   tup = (10, 20, 30, 40)

   tup[0]   -> 10
   tup[2]   -> 30
   tup[-1]  -> 40
   tup[-2]  -> 30


============================================================
5] List vs Tuple

   LIST                         TUPLE
   ----------------------------------------------------------
   Written using []             Written using ()
   Mutable                      Immutable
   Ordered                      Ordered
   Allows duplicates            Allows duplicates
   Supports indexing            Supports indexing
   Supports slicing             Supports slicing
   Many methods                 Only count() and index()


============================================================
6] Important Points

   1) Tuple is ordered.
   2) Tuple is immutable.
   3) Tuple allows duplicate values.
   4) Tuple supports positive and negative indexing.
   5) Tuple supports slicing.
   6) Tuple can store different data types.
   7) Tuple can contain nested collections.
   8) A single-element tuple requires a comma: (10,)
   9) Tuple has two methods: count() and index().
   10) Tuple supports packing and unpacking.
   11) + is used for concatenation.
   12) * is used for repetition.
   13) Tuple elements cannot be directly added, removed,
       or replaced after creation.
"""