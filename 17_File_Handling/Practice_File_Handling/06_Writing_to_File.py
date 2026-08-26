# =========================================================
#             WRITING TO FILE - EXAMPLES
# =========================================================

# Example 1: write()

with open("data.txt", "w") as file:
    file.write("Hello Python")


# Example 2: Write multiple lines using write()

with open("data.txt", "w") as file:
    file.write("Apple\n")
    file.write("Banana\n")
    file.write("Mango\n")


# Example 3: writelines()

lines = [
    "Apple\n",
    "Banana\n",
    "Mango\n"
]

with open("data.txt", "w") as file:
    file.writelines(lines)


# Example 4: Append data

with open("data.txt", "a") as file:
    file.write("Orange\n")


# Example 5: Write data from a list

names = ["Ishwar", "Rahul", "Amit"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


# Example 6: Write numbers

number = 100

with open("number.txt", "w") as file:
    file.write(str(number))


# IMPORTANT:
# write() and writelines() do not automatically add \n.