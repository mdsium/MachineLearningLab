# for loop
for i in range(1, 101):
    print(i, end=" ")
print()

# while loop
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print()

# do-while emulation (Python has no do-while)
i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 100:
        break
print()