def fun(n):
    if n<=2:
        return n
    return fun(n-4) + fun(n-2)
n=int(input())
print(fun(n))