def part(arr,l,h):
    piv = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= piv:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1
def quick(arr,l,h):
    if l < h:
        piv = part(arr,l,h)
        quick(arr, l, piv - 1)
        quick(arr, piv + 1, h)
    return arr
arr=[]
n = int(input())
for i in range(n):
    i = int(input())
    arr.append(i)
print(quick(arr,0,n-1))