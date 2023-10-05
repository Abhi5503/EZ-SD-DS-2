'''
get one number and print sum of digits
'''

n=int(input())
sum = 0
while n>0:
    x = n%10
    sum +=x
    n//=10
print(sum)