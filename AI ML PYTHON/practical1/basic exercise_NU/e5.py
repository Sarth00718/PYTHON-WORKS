'''Write a Python program to check if a triangle is equilateral, isosceles or scalene.'''
def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles"
    else:
        return "Scalene"

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

triangle = triangle_type(side1, side2, side3)
print(f"The triangle is {triangle}.")