from array import array

# Define matrices
matrix_a = [
    array("i", [4, 2, 3]),
    array("i", [4, 5, 6]),
    array("i", [7, 8, 9]),
]

matrix_b = [
    array("i", [9, 8, 7]),
    array("i", [6, 5, 4]),
    array("i", [3, 2, 1]),
]

# Get dimensions
rows_a, cols_a = len(matrix_a), len(matrix_a[0])
rows_b, cols_b = len(matrix_b), len(matrix_b[0])

# Check if matrices can be multiplied
if cols_a != rows_b:
    raise ValueError("Number of columns in matrix A must be equal to the number of rows in matrix B.")

# Initialize result matrix with zeros
result_matrix = [[0] * cols_b for _ in range(rows_a)]

# Perform matrix multiplication
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

# Display the result
for row in result_matrix:
    print(row)
