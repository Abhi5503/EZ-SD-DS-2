def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
#li = list(map(int,input().split())
#arr = [2,5,3,6,4]
arr=[]
n = int(input())
for i in range(n):
    i = int(input())
    arr.append(i)
print(selection(arr))