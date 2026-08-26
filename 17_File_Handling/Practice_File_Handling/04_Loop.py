# =========================================================
#           LOOP THROUGH A FILE - EXAMPLES
# =========================================================

# Example 1: Print every line

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())


# Example 2: Count number of lines

count = 0

with open("data.txt", "r") as file:
    for line in file:
        count += 1

print("Total lines:", count)


# Example 3: Print only lines containing "Python"

with open("data.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())


# Example 4: Process a large file efficiently

with open("large_data.txt", "r") as file:
    for line in file:
        # Process one line at a time
        print(line.strip())