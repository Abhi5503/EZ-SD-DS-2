'''
create an 1d array which should contain numbers bw 10-50
extract and print even numbers and 2 pow values..(log values)
'''

n = int(input("size:"))
arr = []
for i in range(10,n+1):
    arr.append(i)
'''
for i in arr:
    print(i,end=",")
'''
print("the array=",arr)

even_arr=[]
for i in arr:
    if(i%2 == 0):
        even_arr.append(i)
print("even array=",even_arr)

pow_arr=[]
for i in arr:
    for j in range(0,max(even_arr)):
        if(2**j == i):
            pow_arr.append(i)
print("pow arr:",pow_arr)