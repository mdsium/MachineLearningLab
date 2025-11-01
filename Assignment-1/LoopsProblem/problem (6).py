n = int(input("Number: "))
limit = int(input("Up to (e.g., 10): "))
for i in range(1, limit + 1):
    print(f"{n} x {i} = {n * i}")