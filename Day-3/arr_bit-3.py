'''
in the given array,every number occurs twice,only 1 number occurs once
which is that number occuring once
'''
def findsin(ar,n):
    res = ar[0]
    for i in range(1,n):
        res=res^ar[i]
    return res
n=int(input())
ar=[]
for i in range(n):
    i = int(input())
    ar.append(i)
print("the array:",ar)
print(findsin(ar,len(ar)))