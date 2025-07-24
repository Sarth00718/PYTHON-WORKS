''' Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort the array on height.'''

import numpy as np

students = np.array([('Sarth', 175.5, 10),
                     ('Alice', 162.3, 11),
                     ('Heet', 180.2, 10)],dtype=np.dtype([('name', 'S20'), ('height', float), ('class', int)]))
sorted_students = np.sort(students, order='height')

print("Original array:")
print(students)
print("\nArray sorted by height:")
print(sorted_students)