def two_sum(arr, target):
    i = 0
    j = len(arr) - 1  # Initialize j to the last index of the array
    arr.sort()
    while i < j:
        if arr[i] + arr[j] == target:
            return True
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1
    return False

arr = list(map(int, input("Enter space-separated array elements:").split()))
target = int(input("Target:"))
k = two_sum(arr, target)
print(k)