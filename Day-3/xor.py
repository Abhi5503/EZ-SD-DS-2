'''
given n print the xor of all numbers
'''
n=int(input())
xor=0
for i in range(1,n+1):
    xor = xor^i
print(xor)