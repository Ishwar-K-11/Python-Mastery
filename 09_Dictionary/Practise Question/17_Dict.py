"""Dictionary comprehension

Dictionary comprehension is a concise way to create a dictionary in a single line using a loop and optional condition."""


# Normal Way for creating a dictionary
# Using for loop (Creating a dictionary of square of numbers from 1 to 20)
Square = {}
for i in range(1,21):
    Square[i] = i*i

print(Square)


# Dictionary comprehension - Using One Line 
Squares = {i: i*i for i in range(1,11)}
print(Squares)


# With conditions
Marks = {"Englsih":89, "Hindi":78, "Math":98, "Science":88}

# Keep only the 
top = {sub: m for sub, m in Marks.items() if m > 80}
print(top)


# Transform - double for marks 
double = {sub: m*2 for sub, m in Marks.items()}
print(double)


