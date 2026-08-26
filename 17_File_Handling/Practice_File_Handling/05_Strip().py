# =========================================================
#                  strip() - EXAMPLES
# =========================================================

# Example 1: Remove spaces from both sides

text = "   Hello Python   "

print(text.strip())


# Example 2: Remove newline while reading a file

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# Example 3: lstrip() - remove from left

text = "   Hello   "

print(text.lstrip())


# Example 4: rstrip() - remove from right

text = "   Hello   "

print(text.rstrip())


# Example 5: strip() does not remove internal spaces

text = "   Hello    Python   "

print(text.strip())


# Example 6: Clean user input

name = input("Enter your name: ").strip()

print("Hello", name)