# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Binary Search (Array must be sorted)
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = list(map(int, input("Enter elements separated by space: ").split()))
key = int(input("Enter element to search: "))

# Linear
index = linear_search(arr, key)
print("Linear Search Result:", "Found at index" if index != -1 else "Not found", index)

# Binary
arr.sort()
index = binary_search(arr, key)
print("Binary Search Result (on sorted array):", "Found at index" if index != -1 else "Not found", index)
