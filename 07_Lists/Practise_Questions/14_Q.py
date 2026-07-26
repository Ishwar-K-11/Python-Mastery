# take the user input of 3x3 matrix and print it

matrix = []

for i in range(3):
    row = []
    
    for j in range(3):
        num = int(input("Enter number: "))
        row.append(num)
    
    matrix.append(row)

print(matrix)



# Taking user input of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix2 = []

for i in range(rows):
    row1 = []

    for j in range(cols):
        num = int(input(f"Enter element [{i}][{j}]: "))
        row1.append(num)

    matrix2.append(row)

print(matrix2)