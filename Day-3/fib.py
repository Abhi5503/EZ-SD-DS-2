'''
find nth term in fib without iterative
'''
n=int(input())
n1=0
n2=0
if n<0:
    print("not possible")
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n2)