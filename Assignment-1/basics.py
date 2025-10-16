# 1.Write a program to print your name, department, and university.
name ="Md. Sium"
department = "Computer Science and Engineering"
university = "Green University of Bangladesh"

print ("Name:", name)
print ("Department:", department)
print ("University:", university)

# 2.Write a program that takes two integers as input and prints their sum.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number:"))
sum = num1 + num2
print ("the sum of", num1, "and", num2, "is:", sum)


# 3.Write a program that converts temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print (celsius, "degree celsius is equal to", fahrenheit, "degree fahrenheit.")

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