#  Write a program to determine whether a character is a vowel, consonant, digit, or special symbol.
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch.isdigit():
        print("Digit")
    elif ch.isalpha():
        if ch.lower() in "aeiou":
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Special symbol")