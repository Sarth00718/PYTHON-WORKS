'''Write a NumPy program to remove the leading whitespaces of all the elements of a given array.'''
import numpy as np

array_with_spaces = np.array(['  hello', ' world', '   numpy'])

trimmed_array = np.core.defchararray.lstrip(array_with_spaces)

print("Original Array with Spaces:")
print(repr(array_with_spaces))
print("\nArray with Leading Whitespaces Removed:")
print(repr(trimmed_array))