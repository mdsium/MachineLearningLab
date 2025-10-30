# Write a program to find the greatest number among three numbers using if–else statements.
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a >= b and a >= c:
    print("Greatest:", a)
elif b >= a and b >= c:
    print("Greatest:", b)
else:
    print("Greatest:", c)   