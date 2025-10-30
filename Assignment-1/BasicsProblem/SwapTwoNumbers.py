# 7. Write a program to swap two numbers using a temporary variable
x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))

print("Before swap -> x: ", x, "y:", y)
temp = x
x = y
y = temp 
print("After swap -> x: ", x, "y: ", y)

# 8. Write a program to swap two numbers without using a temporary variable
x = int(input("Enter a Number: "))
y = int(input("Enter a Number: "))

print("Before swap -> x: ", x, "y:", y)
x,y = y,x
print("After swap -> x: ", x, "y: ", y)
