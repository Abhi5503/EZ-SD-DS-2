'''
swap 2 numbers using xor
'''
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b

print("a:",a,"b:",b)