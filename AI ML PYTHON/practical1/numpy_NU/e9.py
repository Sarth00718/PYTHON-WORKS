'''Write a NumPy program to capitalize the first letter, lowercase, uppercase, swapcase, title-case of all the elements of a given array.'''
import numpy as np

array_of_strings = np.array(['hello', 'world', 'numpy'])

capitalized_array = np.core.defchararray.capitalize(array_of_strings)
lowercase_array = np.core.defchararray.lower(array_of_strings)
uppercase_array = np.core.defchararray.upper(array_of_strings)
swapcase_array = np.core.defchararray.swapcase(array_of_strings)
titlecase_array = np.core.defchararray.title(array_of_strings)

print("Original Array:", array_of_strings)
print("Capitalized Array:", capitalized_array)
print("Lowercase Array:", lowercase_array)
print("Uppercase Array:", uppercase_array)
print("Swapcase Array:", swapcase_array)
print("Title-case Array:", titlecase_array)