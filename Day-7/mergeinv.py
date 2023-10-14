c = 0  # Declare c as a global variable

def merge_inv(lst):
    global c  # Declare c as a global variable
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        # Recursively call merge_inv on left and right sublists
        left = merge_inv(left)
        right = merge_inv(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                c += len(left) - i  # Increment c when there's an inversion
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

    return lst

lst = list(map(int, input().split()))
#merge_inv(lst)
print(merge_inv(lst))
print("Number of inversions:", c)

