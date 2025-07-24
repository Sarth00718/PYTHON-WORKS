'''Write a NumPy program to concatenate element-wise two arrays of string.'''
import numpy as np

array1 = np.array(['Hello', 'World', 'NumPy'])
array2 = np.array([' is', ' a', ' library'])

# Concatenate the arrays element-wise
concatenated_array = np.core.defchararray.add(array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Concatenated Array element-wise:", concatenated_array)