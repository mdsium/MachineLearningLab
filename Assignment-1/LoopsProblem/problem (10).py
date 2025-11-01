n = int(input("n: "))
def fact(d):
    f = 1
    for i in range(2, d + 1):
        f *= i
    return f

x = n
s = 0
if x == 0:
    s = fact(0)
else:
    while x > 0:
        s += fact(x % 10)
        x //= 10
print("Strong number" if s == n else "Not a Strong number")