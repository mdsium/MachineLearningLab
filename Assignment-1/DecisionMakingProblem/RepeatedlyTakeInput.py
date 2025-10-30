# Write a program to use goto to repeatedly take input from the user until 0 is entered.
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        print("Stopped.")
        break
    print("You entered:", n)