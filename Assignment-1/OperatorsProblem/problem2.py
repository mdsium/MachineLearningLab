# 2.  Write a program to find the maximum of three numbers using logical operators.

num1 = int(input("Enter an Number: "))
num2 = int(input("Enter an Number: "))
num3 = int(input("Enter an Number: "))

max = num1 
if num2 > max and num2 >= num3:
    max = num2
if num3 > max and num3 >= num2:
    max = num3
print("Max is: ", max)
