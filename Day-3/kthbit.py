'''
for the given no n;check the kth bit is set or not
'''
def kthbit(n, k):
    return (n & (1 << k)) != 0
n = 12
k = 2 
result = kthbit(n, k)
print(f"The {k}th bit of {n} is set: {result}")
