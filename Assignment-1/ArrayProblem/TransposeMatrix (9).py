rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix elements:")
matrix = [[int(input()) for j in range(cols)] for i in range(rows)]

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print("Transpose of the matrix:")
for row in transpose:
    print(row)
