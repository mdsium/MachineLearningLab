# Write a program to check whether a number is even or odd using both modulo and bitwise operators.
num = int(input("Enter an number: "))
if num % 2 == 0:
    print("Even Number: ")
else:
    print("odd Number: ")

if num & 1 == 0:
    print("Even number: ")
else:
    print("Odd Number: ")