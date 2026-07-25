# 3x3 Matrix
"""
matrix = [
    [10,20,30],
    [50,60,80],
    [12,11,83]
]

print(matrix[1])
print(matrix[2])
print(matrix[0][1])
print(matrix[1][2])
print(matrix[2][0])
print(matrix[0][0])

"""

"""
Printing the total of the matrix
"""

matrix = [
    [10,20,30],
    [50,60,80],
    [12,11,83]
]
total = 0
for i in range(0,3):
    for j in range(0,3):
        total += matrix[i][j]

print(total)



# Printing 4x5 Matrix
matrix2 =[
    [1,6,8,9,6],
    [3,7,8,6,4],
    [2,9,7,5,6],
    [2,4,7,5,1]
]
rows = len(matrix2)
column = len(matrix2[0])
for i in range(0,rows):
    for j in range(0,column):
        print(matrix2[i][j],end=" ")
    print() 


