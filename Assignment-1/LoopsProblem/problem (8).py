n = int(input("n: "))
if n < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    print("Prime" if is_prime else "Not prime")