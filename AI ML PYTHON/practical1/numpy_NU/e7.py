'''Write a NumPy program to multiply a 5x3 matrix by a 3x2 matrix and create a real matrix product.'''
import numpy as np

matrix_a = np.random.random((5, 3))
matrix_b = np.random.random((3, 2))

matrix_product = np.dot(matrix_a, matrix_b)

print("Matrix A (5x3):")
print(matrix_a)
print("\nMatrix B (3x2):")
print(matrix_b)
print("\nMatrix Product (5x2):")
print(matrix_product)