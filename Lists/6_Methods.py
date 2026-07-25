"""
List methods are built-in methods that operate directly on a list.
They allow you to modify the list in place, meaning the original list is changed instead of creating a new one.
Unlike the built-in sorted() function, methods such as sort() modify the original list.

"""

"""
1] Adding Elements
   1) .append()
        Adds a single element at the end of the list
        fruits = ["apple", "banana]
        fruits.append("orange")
        print(fruits) #Output ["apple", "banana","orange"]

    2) .insert()
        Adds element at the specific index. The frist argument is index and then second one is value
        fruits = ["apple", "banana]
        fruits.insert(1,"orange")
        print(fruits) #Output ["apple","orange", "banana"]

2] Removing Element
    1) .remove() - Remove by Value
        removes the frist occurence of the element of a specific value from the list
        if the value is not present in the list it throws a value error
        fruits = ["apple","orange", "banana"]
        fruits.remove("orange")
        print(fruits) #Output ["apple", "banana"]

    2) .pop() - Remove by index
        Removes and return the element at the given index
        if index is not provided automatically remove the last element of the index
        fruits = ["apple","orange", "banana"]
        fruits.pop()
        fruits.pop(1)
        print(fruits) #Output ["apple"]

3] Sorting

    1) .sort() - Ascending Order
        Sorts the list in ascending order (smallest to largest or A to Z)
        It modifies the original list.
        nums = [5, 2, 8, 1]
        nums.sort()
        print(nums) #Output [1, 2, 5, 8]

    2) .sort(reverse=True) - Descending Order
        Sorts the list in descending order (largest to smallest or Z to A)
        It modifies the original list.
        nums = [5, 2, 8, 1]
        nums.sort(reverse=True)
        print(nums) #Output [8, 5, 2, 1]


4] Reversing

    1) .reverse()
        Reverses the order of the elements in the list.
        It does not sort the list; it only reverses the current order.
        nums = [1, 2, 3, 4]
        nums.reverse()
        print(nums) #Output [4, 3, 2, 1]


5] Searching

    1) .index()
        Returns the index of the first occurrence of the specified value.
        If the value is not present, it throws a ValueError.
        fruits = ["apple", "orange", "banana", "orange"]
        print(fruits.index("orange")) #Output 1

    2) in Operator
        Checks whether a value exists in the list.
        Returns True if found, otherwise False.
        fruits = ["apple", "orange", "banana"]
        print("orange" in fruits) #Output True
        print("grapes" in fruits) #Output False


6] Counting

    1) .count()
        Returns the number of times a specified value appears in the list.
        fruits = ["apple", "orange", "banana", "orange", "orange"]
        print(fruits.count("orange")) #Output 3

7] Copying

    1) .copy()
        Creates a shallow copy of the list.
        fruits = ["apple", "banana"]
        new_list = fruits.copy()
        print(new_list) #Output ["apple", "banana"]


8] Clearing

    1) .clear()
        Removes all the elements from the list.
        fruits = ["apple", "banana", "orange"]
        fruits.clear()
        print(fruits) #Output []


"""
