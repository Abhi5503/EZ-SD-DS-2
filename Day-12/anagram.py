def anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    xor=0
    for i in s1:
        xor^=ord(i)
    for j in s2:
        xor^=ord(j)
    if xor == 0:
        return True
    return False
s1 = input()
s2 = input()
res = anagram(s1,s2)
print(res)   