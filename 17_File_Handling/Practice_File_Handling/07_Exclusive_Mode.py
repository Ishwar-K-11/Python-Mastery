# =========================================================
#              EXCLUSIVE MODE "x" - EXAMPLES
# =========================================================

# Example 1: Create a new file

try:
    with open("newfile.txt", "x") as file:
        file.write("Hello Python")

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")


# Example 2: Safe file creation

filename = "report.txt"

try:
    with open(filename, "x") as file:
        file.write("New Report")

    print("Report created.")

except FileExistsError:
    print("Report already exists.")


# "x" vs "w"
#
# "x" -> Creates only if the file does not exist.
# "w" -> Creates or overwrites the file.