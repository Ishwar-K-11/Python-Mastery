# Printing the Upper triangle elements of matrix and replce lower triangle with the * (star)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        if i <= j:
            print(matrix[i][j], end=" ")
        else:
            print("*", end=" ")

    print()

print()
print()
print()
print()


# printing the same for the 5x5 matrix

matrix2 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5]
]

for i in range(5):
    for j in range(5):
        if i >= j:
            print(matrix2[i][j], end=" ")
        else:
            print("*",end=" ")
    print()

print()
print()
print()
print()

# Printing only diagonal elements
matrix3 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [1, 2, 3, 4, 5]
]

for i in range(5):
    for j in range(5):
        if i == j:
            print(matrix3[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
