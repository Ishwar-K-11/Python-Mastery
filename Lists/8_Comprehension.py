"""
List Comprehension

    1) Basic List Comprehension
        Creates a new list by applying an expression to each element of an iterable.
        It returns a new list and does not modify the original list.
        Syntax:
        new_list = [expression for item in iterable]

        nums = [1, 2, 3, 4, 5]
        squares = [num**2 for num in nums]
        print(squares) #Output [1, 4, 9, 16, 25]

    2) List Comprehension with Condition
        Creates a new list by selecting only those elements that satisfy a condition.
        It returns a new list and does not modify the original list.
        Syntax:
        new_list = [expression for item in iterable if condition]

        nums = [1, 2, 3, 4, 5, 6]
        evens = [num for num in nums if num % 2 == 0]
        print(evens) #Output [2, 4, 6]

    3) List Comprehension with if-else
        Creates a new list by applying different expressions based on a condition.
        It returns a new list and does not modify the original list.
        Syntax:
        new_list = [expression_if_true if condition else expression_if_false for item in iterable]

        nums = [1, 2, 3, 4, 5]
        result = ["Even" if num % 2 == 0 else "Odd" for num in nums]
        print(result) #Output ['Odd', 'Even', 'Odd', 'Even', 'Odd']
"""

# Examples 01 
lst = [i for i in range(1,11)]
print(lst)

# Example 02
lst1 = [i * i for i in range(1,11)]   # where you can do i-x  or i+x or something else
print(lst1)

lst2 = [i for i in range(1,11) if i % 2 == 0]
print(lst2)

lst3 = [i for i in range(1,11) if i % 2 == 0 and i % 3 == 0]
print(lst3)

def is_prime(num):
    factors = 0
    for i in range(1,num+1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    return False

new_list = [i for i in range(2,101) if is_prime(i)]
print(new_list)

