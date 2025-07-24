'''Write a NumPy program to compute logarithm of the sum of exponentiations of the inputs, sum of exponentiations of the inputs in base-2.'''
import numpy as np

arr = np.array([2, 3, 4])

log_sum_exp = np.log(np.sum(np.exp(arr)))

log_sum_exp_base2 = np.log2(np.sum(np.exp(arr)))

print("Original array:", arr)
print("Logarithm of the sum of exponentiations:", log_sum_exp)
print("Logarithm of the sum of exponentiations in base-2:", log_sum_exp_base2)