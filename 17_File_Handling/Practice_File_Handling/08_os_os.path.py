# =========================================================
#              os AND os.path - EXAMPLES
# =========================================================

import os


# Example 1: Check whether a path exists

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")


# Example 2: Check whether it is a file

if os.path.isfile("data.txt"):
    print("It is a file")


# Example 3: Check whether it is a directory

if os.path.isdir("Documents"):
    print("It is a directory")


# Example 4: Get file size

if os.path.exists("data.txt"):
    size = os.path.getsize("data.txt")
    print("Size:", size, "bytes")


# Example 5: Get file name

path = "Documents/Projects/data.txt"

print("File name:", os.path.basename(path))


# Example 6: Get directory name

print("Directory:", os.path.dirname(path))


# Example 7: Join paths

path = os.path.join(
    "Documents",
    "Projects",
    "data.txt"
)

print(path)


# Example 8: Get absolute path

print(os.path.abspath("data.txt"))


# Example 9: Split filename and extension

name, extension = os.path.splitext("data.txt")

print("Name:", name)
print("Extension:", extension)


# Example 10: Rename a file

if os.path.exists("old.txt"):
    os.rename("old.txt", "new.txt")


# Example 11: Delete a file

if os.path.exists("data.txt"):
    os.remove("data.txt")


# Example 12: Create a directory

if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")


# Example 13: Remove an empty directory

if os.path.exists("MyFolder"):
    os.rmdir("MyFolder")


# Example 14: List directory contents

if os.path.exists("Documents"):
    for item in os.listdir("Documents"):
        print(item)