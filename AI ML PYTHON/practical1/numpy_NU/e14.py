'''Write a NumPy program to find the dot product of two arrays of different dimensions'''
import numpy as np

array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])
array2 = np.array([7, 8, 9])
dot_product = np.dot(array1, array2)

print("Array 1:")
print(array1)

print("\nArray 2:")
print(array2)

print("\nDot Product:")
print(dot_product)