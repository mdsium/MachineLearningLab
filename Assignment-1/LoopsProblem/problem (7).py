L = int(input("Lower: "))
R = int(input("Upper: "))
start = L if L % 2 == 0 else L + 1
for x in range(start, R + 1, 2):
    print(x, end=" ")
print()