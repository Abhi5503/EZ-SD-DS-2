def sum_arr(matrix):
    add=0
    for i in matrix:
        add+=i
    return add

n=int(input())
matrix=[]
for i in range(n):
    ele=int(input("ele:"))
    matrix.append(ele)
k=sum_arr(matrix)
print(k)
        