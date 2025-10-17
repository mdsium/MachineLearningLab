n = int(input("n: "))
if n <= 1:
    print("Not perfect")
else:
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    print("Perfect" if s == n else "Not perfect")