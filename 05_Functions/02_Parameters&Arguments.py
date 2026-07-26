"""
PARAMETERS AND ARGUMENTS


Parameter
    A parameter is a variable written in the function definition.
    It acts as a placeholder to receive a value.

Argument
    An argument is the actual value passed to the function when it is called.

Syntax
    def function_name(parameter):
        statements

    function_name(argument)



Example 1
    def greet(name):
        print("Hello", name)

    greet("Ishwar")

Output
Hello Ishwar


Example 2
    def add(a, b):
        print(a + b)

    add(10, 20)

    Output
    30


Multiple Parameters
    def student(name, age):
        print(name, age)

    student("Rahul", 20)

    Output
    Rahul 20

Types of Arguments

    1. Positional Arguments
        Values are matched according to their position.

Example
    def add(a, b):
        print(a + b)
    add(5, 10)

    Output
    15

2. Keyword Arguments
   Values are passed using parameter names.

Example

def student(name, age):
    print(name, age)

student(age=20, name="Rahul")

Output
Rahul 20

3. Default Arguments
   A parameter is given a default value.

Example

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Ishwar")

Output
Hello Guest
Hello Ishwar

Important Points

    1. Parameters are written in the function definition.
    2. Arguments are supplied during the function call.
    3. The number of arguments should match the number of required parameters.
    4. Keyword arguments can be passed in any order.
    5. Default arguments are used when no value is provided.
"""
