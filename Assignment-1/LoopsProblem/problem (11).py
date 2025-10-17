n = int(input("n: "))
x = abs(n)
s = 0
p = 1
if x == 0:
    s, p = 0, 0
else:
    while x > 0:
        d = x % 10
        s += d
        p *= d
        x //= 10
print("Spy number" if s == p else "Not a Spy number")