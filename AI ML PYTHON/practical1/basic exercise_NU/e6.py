'''Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''

number = int(input("Enter a number: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")



