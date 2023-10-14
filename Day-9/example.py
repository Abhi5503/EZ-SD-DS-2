'''
input: 7564168
example: separate odd place integers:5 4 6
you have to return a 4 digit OTP by squaring the digits
digits from above ex: 5 4 6
Squares: 25, 16, 36
so OTP to be returned in first four digits: 2516
'''
n = int(input())
arr = []

for i in range(n):
    i = int(input())
    arr.append(i)

oddp = [arr[i] for i in range(len(arr)) if i % 2 != 0]
print(oddp)

sqr = [oddp[i] * oddp[i] for i in range(len(oddp))]
print(sqr)

otp = str(sqr)
otp1 = ''.join(filter(str.isdigit, otp))[:4]
print(otp1)