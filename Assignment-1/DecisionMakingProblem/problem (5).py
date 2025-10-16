# Write a program to create a simple calculator using switch–case statements.
a = float(input("First number: "))
op = input("Operator (+, -, *, /): ").strip()
b = float(input("Second number: "))

match op:
    case '+':
        print("Result:", a + b)
    case '-':
        print("Result:", a - b)
    case '*':
        print("Result:", a * b)
    case '/':
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result:", a / b)
    case _:
        print("Invalid operator")