"""
RETURN STATEMENT

The return statement is used to send a value back from a function.
Once the return statement executes, the function immediately ends.

Syntax

def function_name():
    return value

result = function_name()

Example 1

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

Output
30

Example 2

def square(num):
    return num * num

print(square(5))

Output
25

Returning Multiple Values

def calculate(a, b):
    return a + b, a - b

sum_value, difference = calculate(10, 5)

print(sum_value)
print(difference)

Output
15
5

Function Without Return

def greet():
    print("Hello")

value = greet()
print(value)

Output
Hello
None

Important Points

1. return sends a value back to the caller.
2. A function can return any data type.
3. Multiple values can be returned using commas.
4. Code written after return is never executed.
5. If no return statement is used, Python automatically returns None.
"""
