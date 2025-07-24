''' 4.Write a NumPy program to partition a given array in a specified position and move all the smaller elements values to the left of the partition, and the remaining values to the right, in arbitrary order (based on random choice).'''
import numpy as np

def partition_array(arr, partition_index):
    # Partition the array
    np.random.shuffle(arr)
    smaller_values = arr[arr < arr[partition_index]]
    larger_values = arr[arr >= arr[partition_index]]
    
    # Concatenate the smaller and larger values
    result_array = np.concatenate((smaller_values, larger_values))
    
    return result_array

# Create a sample array
original_array = np.array([45, 12, 78, 32, 56])

# Choose the partition index (position to partition the array)
partition_index = 2

# Partition the array and print the result
result = partition_array(original_array, partition_index)

print("Original array:", original_array)
print(f"Array after partitioning at index {partition_index}:",result)