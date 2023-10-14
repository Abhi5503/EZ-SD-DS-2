'''
str1=input()
print(str1[::-1])
'''
'''
s=input()
s.split()
temp=[]
spc='[@_!#$%^&*()<>?/\|}{~:]'
for i in range(len(s)):
    if s[i] in spc:
        temp[i]=s[i]
'''
s = input()
temp = list(s)
spc = '[@_!#$%^&*()<>?/\|}{~:]'

i = 0
j = len(s) - 1

while i < j:
    if s[i] in spc:
        i += 1
    elif s[j] in spc:
        j -= 1
    else:
        temp[i], temp[j] = temp[j], temp[i]
        i += 1
        j -= 1

reversed_string = ''.join(temp)
print(reversed_string)
