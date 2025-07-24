'''10.	Write a NumPy program to insert a space between characters of all the elements of a given array.'''
import numpy as np

array_of_strings = np.array(['hello', 'world', 'numpy'])
spaced_array = np.core.defchararray.add(' ', array_of_strings)

print("Original Array:", array_of_strings)
print("Array with Space Between Characters:",spaced_array)