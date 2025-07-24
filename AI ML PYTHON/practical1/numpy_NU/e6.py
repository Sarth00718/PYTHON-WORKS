'''Write a NumPy program to calculate the absolute value element-wise'''
import numpy as np

arr = np.array([-2, -5, 0, 3, -1])
abs_values = np.abs(arr)

print("Original array:", arr)
print("Absolute values element-wise:",abs_values)