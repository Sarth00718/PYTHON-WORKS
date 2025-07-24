'''Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equa '''

import numpy as np

students = np.array([('John', 175.5, 10),
                     ('Sarth', 180.2, 10),
                     ('Heet', 170.0, 11)],dtype=np.dtype([('name', 'S20'), ('height', float), ('class', int)]))

# Sort the array first by 'class', then by 'height'
sorted_students = np.sort(students, order=['class', 'height'])

print("Original array:")
print(students)
print("\nArray sorted by class, then by height if classes are equal:")
print(sorted_students)