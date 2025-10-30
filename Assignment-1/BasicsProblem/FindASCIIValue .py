# 6. Write a program to find the ASCII value of a character.
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    print("ASCII value of", ch, "is", ord(ch))