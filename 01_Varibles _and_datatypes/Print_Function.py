# Different types of print function in python
age = 10
name = "ishwar"
CGPA = 9.5

print("Hello", name)

# printing With The F-String gives you incorrect and good output
# also you can peform the mathematical operations inside the print function using f-string.
print(f"My name is {name}, I am {age+10} years old and my CGPA is {CGPA}")

# print("My name is ",name "I am ",age "years old and my CGPA is",CGPA)
# Gives Wrong output because of missing commas in between the variables and strings.

print(name, age, CGPA, sep=" | ")
# This will print the variables with a separator of your choice. In this case, it is a pipe symbol.

print(name, end=" ")
print(age, end=" ")
print(CGPA)

print('Hello "am" ishwar')
print('MY name is "ISHWAR"')
