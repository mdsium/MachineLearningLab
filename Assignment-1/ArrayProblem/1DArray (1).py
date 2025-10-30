n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

print("Array elements are:", arr)
