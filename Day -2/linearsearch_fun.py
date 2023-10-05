'''
linear search in python
'''

def linear(arr,key):
    for i in range (len(arr)):
        if(arr[i]==key):
            return 1
    return 0

n=int(input("size:"))
arr=[]
for i in range(n):
    ele=int(input("ele:"))
    arr.append(ele)
key=int(input("key:"))
k=linear(arr,key)
if(k==1):
    print("key ele found")
else:
    print("key ele not found")
