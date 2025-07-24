'''Write a NumPy program to get the indices of the sorted elements of a given array.'''
import numpy as np

arr = np.array([45, 12, 78, 32, 56])

sorted_indices = np.argsort(arr)

print("Original array:",arr)
print("Indices of sorted elements:",sorted_indices)