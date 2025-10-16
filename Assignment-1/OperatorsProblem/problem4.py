# 4. Write a program to find the minimum of two numbers using the conditional (ternary) operator.
x = float(input("x: "))
y = float(input("y: "))

mn = x if x < y else y
print("Min is:", mn)