# =========================================================
#                  PATHLIB - EXAMPLES
#              MODERN WAY TO HANDLE PATHS
# =========================================================

from pathlib import Path


# Example 1: Create a Path object

path = Path("data.txt")

print(path)


# Example 2: Check whether path exists

if path.exists():
    print("File exists")


# Example 3: Check file and directory

if path.is_file():
    print("It is a file")

folder = Path("Documents")

if folder.is_dir():
    print("It is a directory")


# Example 4: Write to a file

path.write_text("Hello Python")


# Example 5: Read from a file

data = path.read_text()

print(data)


# Example 6: Append to a file

with path.open("a") as file:
    file.write("\nHello World")


# Example 7: Create an empty file

new_file = Path("newfile.txt")

new_file.touch()


# Example 8: Delete a file

if new_file.exists():
    new_file.unlink()


# Example 9: Rename a file

old_file = Path("old.txt")

if old_file.exists():
    old_file.rename("new.txt")


# Example 10: Create a directory

folder = Path("Documents")

if not folder.exists():
    folder.mkdir()


# Example 11: Create nested directories

project_folder = Path("Projects/Python/FileHandling")

project_folder.mkdir(parents=True, exist_ok=True)


# Example 12: List directory contents

if folder.exists():
    for item in folder.iterdir():
        print(item)


# Example 13: Join paths using /

file_path = Path("Documents") / "Projects" / "data.txt"

print(file_path)


# Example 14: File name, stem, extension and parent

path = Path("Documents/data.txt")

print("Name:", path.name)
print("Stem:", path.stem)
print("Suffix:", path.suffix)
print("Parent:", path.parent)


# Example 15: Find all .txt files

folder = Path("Documents")

for file in folder.glob("*.txt"):
    print(file)


# Example 16: Recursive search

for file in folder.rglob("*.txt"):
    print(file)


# Example 17: File size

if path.exists():
    print("Size:", path.stat().st_size, "bytes")


# Example 18: Absolute path

print(path.resolve())


# Example 19: Change extension

csv_path = path.with_suffix(".csv")

print(csv_path)


# Example 20: Modern practical example

file = Path("student.txt")

if not file.exists():
    file.write_text("Ishwar\nComputer Science")

content = file.read_text()

print(content)