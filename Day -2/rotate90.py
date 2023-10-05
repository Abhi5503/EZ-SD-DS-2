'''
p)implement a 2d array and rotate the matrix 90deg
What is stack and heap mem where are these used?
'''

def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]

row=int(input("row:"))
column=int(input("column:"))
matrix = []
for i in range(row):
    row = []
    for j in range(column):
        ele = int(input("ele:"))
        row.append(ele)
    matrix.append(row)
for row in matrix:
    print("non rotated:",row)
rotate(matrix)
for row in matrix:
    print("rotated 90 deg:",row)
    