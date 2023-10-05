def quick_sort(arr):
    if len(arr) <= 1:
        return arr      
    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle of the array)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)


arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)
