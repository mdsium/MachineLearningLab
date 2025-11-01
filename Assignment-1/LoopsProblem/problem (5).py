n = int(input("n: "))
x = abs(n)
count = 1 if x == 0 else 0
s = 0
while x > 0:
    s += x % 10
    x //= 10
    count += 1
print("Digits:", count if n != 0 else 1)
print("Sum of digits:", s if n != 0 else 0)