# 4.Write a program to calculate area and perimeter of rectangle, circle, and triangle.
import math
print("Choose shape: 1.Rectangle 2.circle 3.Triangle")
choice = input("Enter choice(1/2/3): ").strip()

if choice == "1":
    length = float(input("Enter length of rectangle:"))
    width = float(input("Enter width of rectangle:"))
    area = length * width
    perimeter = 2 * (length + width)
    print("Area of rectangle:", area)
    print("Perimeter of rectangle: ", perimeter)

elif choice == "2":
    r = float(input("Enter radius of circle: "))
    area = math.pi *r * r
    circumference = 2 * math.pi * r
    print("Area of circle:", area)
    print("Circumference of circle:", circumference)
    
elif choice == "3":
    a = float(input("enter side a of triangle: "))
    b = float(input("enter side b of triangle: "))
    c = float(input("enter side c of triangle: "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    perimeter = a+b+c
    print ("Area of triangle: ", area)
    print ("prerimeter of trinagle: ", perimeter)
else:
    print ("Invalid input")