def max_three_sum(arr):
    arr.sort()  
    n = len(arr)
    max_sum = max(arr)
    for left in range(n - 2):
        curr = left + 1
        right = n - 1
        while curr < right:
            curr_sum = arr[left] + arr[curr] + arr[right]
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum <= max_sum:
                curr += 1
            if curr_sum >= max_sum:
                right -= 1
    return max_sum

arr = list(map(int,input().split()))
result = max_three_sum(arr)
print("Maximum three-element sum:", result)

