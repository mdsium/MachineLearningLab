arr = list(map(int, input("Enter elements separated by space: ").split()))

pos = neg = zero = even = odd = 0
for num in arr:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Positive:", pos)
print("Negative:", neg)
print("Zero:", zero)
print("Even:", even)
print("Odd:", odd)
