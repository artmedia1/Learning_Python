#1) Create a program to calculate the area and circumference of a circle. Ask the user for the radius.
from cmath import pi
import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * pi * radius
area = pi * (radius ** 2)

print("Circumference: " + str(circumference), "Area: " + str(area), sep='\n')