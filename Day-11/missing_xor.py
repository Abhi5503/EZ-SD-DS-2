def xor_missingnum(arr):
    n = len(arr)
    tot = 0
    rep = 0
    for i in range(1,n+1):
        rep^=i
    for num in (arr):
        tot^=num
    repeated = tot^rep
    return repeated
    #return tot
arr = list(map(int,input().split(", ")))
k=xor_missingnum(arr)
print(k)