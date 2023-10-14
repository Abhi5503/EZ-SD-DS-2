def sliding_window(arr,k):
    n = len(arr)
     if k>n:
        return
    maxs = max(arr)
    curr_sum = maxs
    for i in range(k,n):
        curr_sum = curr_sum - arr[i-k] + arr[i]
        maxs=max(maxs,curr_sum)
    return maxs
arr = list(map(int,input().split()))
k = int(input())
result = sliding_window(arr,k)
print(' Maximum',k,"element sum:",result)