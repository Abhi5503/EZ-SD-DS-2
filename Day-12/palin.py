'''
1.count no of palindromic substring
2.count longest palindromic substring
3.smallest palindromic substring which is not 1 in length
no of sub strings in a string = (n*(n+1))/2
'''
def palin(s):
    temp = s
    for i in range(len(s)):
        for j in range(i,len(s)):
            if temp == s[::-1]:
                return True
    return False
s = input()
res = palin(s)
print(res)