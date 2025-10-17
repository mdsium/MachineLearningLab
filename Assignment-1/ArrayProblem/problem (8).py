rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix A:")
A = [[int(input()) for j in range(cols)] for i in range(rows)]

print("Enter elements of Matrix B:")
B = [[int(input()) for j in range(cols)] for i in range(rows)]

# Add matrices
result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

print("Sum of matrices:")
for row in result:
    print(row)
