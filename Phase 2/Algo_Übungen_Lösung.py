# Bubble Sort
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    print("\n--- Bubble Sort ---")
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"Schritt {i}.{j}: {arr}")
    return arr

# Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()
    print("\n--- Insertion Sort ---")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Schieben bei i={i}: {arr}")
        arr[j + 1] = key
        print(f"Einfügen bei i={i}: {arr}")
    return arr

# Merge Sort
def merge_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], depth+1)
    right = merge_sort(arr[mid:], depth+1)
    merged = merge(left, right)
    print("  " * depth + f"Mergen: {merged}")
    return merged

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr, depth=0):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    smaller = [x for x in arr[1:] if x <= pivot]
    bigger = [x for x in arr[1:] if x > pivot]
    print("  " * depth + f"Pivot {pivot}: {smaller} + [{pivot}] + {bigger}")
    return quick_sort(smaller, depth+1) + [pivot] + quick_sort(bigger, depth+1)


zahlen = [5, 2, 9, 1, 5, 6]

print("Ursprüngliche Liste:", zahlen)
print("Ende Bubble Sort:", bubble_sort(zahlen))
print("Ende Insertion Sort:", insertion_sort(zahlen))
print("\n--- Merge Sort ---")
print("Ende Merge Sort:", merge_sort(zahlen))
print("\n--- Quick Sort ---")
print("Ende Quick Sort:", quick_sort(zahlen))