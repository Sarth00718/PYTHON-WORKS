'''Write a NumPy program to sort a given array of shape 2 along the first axis, last axis and on flattened array.'''
import numpy as np

array_2d = np.array([[3, 1, 5],
                     [2, 8, 4]])

sorted_first_axis = np.sort(array_2d, axis=0)
sorted_last_axis = np.sort(array_2d, axis=1)
sorted_flattened = np.sort(array_2d.flatten())

print("Original 2D Array:")
print(array_2d)

print("\nSorted along the first axis:")
print(sorted_first_axis)

print("\nSorted along the last axis:")
print(sorted_last_axis)

print("\nSorted flattened array:")
print(sorted_flattened)