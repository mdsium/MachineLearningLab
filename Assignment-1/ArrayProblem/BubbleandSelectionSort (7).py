arr = list(map(int, input("Enter elements separated by space: ").split()))

# Bubble Sort
bubble = arr.copy()
for i in range(len(bubble)):
    for j in range(0, len(bubble) - i - 1):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print("Bubble Sorted:", bubble)

# Selection Sort
selection = arr.copy()
for i in range(len(selection)):
    min_index = i
    for j in range(i + 1, len(selection)):
        if selection[j] < selection[min_index]:
            min_index = j
    selection[i], selection[min_index] = selection[min_index], selection[i]
print("Selection Sorted:", selection)
