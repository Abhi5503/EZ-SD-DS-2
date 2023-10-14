def count_sort(l):
    n = len(l)
    count = [0]*n
    res= [0]*n
    for i in range(n):
        count[l[i]]+=1
    for i in range(1,n):
        count[i]+=count[i-1]
    k = n-1
    while k>=0:
        res[count[l[k]]-1]=l[k]
        count[l[k]]-=1
        k-=1
    for i in range(0,n):
        l[i]=res[i]
l = list(map(int,input().split()))
count_sort(l)
for i in l:
    print(l[i],end = " ")
        