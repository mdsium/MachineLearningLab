n = int(input("n: "))
rev = 0
x = abs(n)
while x > 0:
    rev = rev * 10 + x % 10
    x //= 10
rev = -rev if n < 0 else rev
print("Reversed =", rev)