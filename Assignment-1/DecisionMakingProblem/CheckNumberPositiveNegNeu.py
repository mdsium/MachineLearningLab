# Write a program to check whether a number is positive, negative, or neutral.
n = float(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Neutral (zero)")