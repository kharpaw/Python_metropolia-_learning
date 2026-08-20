# Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.

length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of the rectangle: "))

perimeter = 2 * (length + width)
area = length * width

print(perimeter)
print(area)