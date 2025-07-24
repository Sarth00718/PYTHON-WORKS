'''Write a NumPy program to create a 5x5 array with random values and sort each row'''
import numpy as np

random_array = np.random.rand (5, 5)

sorted_array = np.sort(random_array, axis=1)

print("Original 5x5 Array:")
print(random_array)

print("\n Sorted 5x5 Array (Each row sorted):")
print(sorted_array)