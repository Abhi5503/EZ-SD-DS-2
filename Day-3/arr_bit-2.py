'''
after creating an array,find the smallest missing positive
integer
Time Complexity: O(n^2)
Space Complexity: O(n)
'''
n=int(input())
arr=[]
for i in range(n):
    i= int(input())
    arr.append(i)
print("the array:",arr)
pos=[]
neg=[]
for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)
print("positive array:",pos)
print("negative array:",neg)
for i in range(0,len(pos)):
    for j in range(i+1,len(pos)):
        if pos[i]>=pos[j]:
            temp=pos[i]
            pos[i]=pos[j]
            pos[j]=temp
print("sorted array:",pos)

miss=1
while miss in pos:
    miss+=1
print(miss)
