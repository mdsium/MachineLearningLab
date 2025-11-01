s = input("Enter a string: ")
count = 0
for _ in s:
    count += 1
print("Manual length:", count)
print("Using len():", len(s))
