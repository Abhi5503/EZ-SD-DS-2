def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        # Recursively sort both sublists
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the sorted sublists back into the original list
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Check if any elements were left in either sublist
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

# Take multiple numbers as input
lst = list(map(int, input("Enter space-separated numbers: ").split()))

# Sort the input list using merge sort
merge_sort(lst)

# Print the sorted list
print("Sorted list:", lst)
