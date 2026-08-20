# 2 Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
import math

radius = int(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print(f"{area:.2f}")