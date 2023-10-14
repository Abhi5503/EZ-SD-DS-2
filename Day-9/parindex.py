def demo(s):
    c=0
    l=[]
    for i in s:
        if i=='[' or i=='{' or i=='(':
            l.append(i)
            c+=1
            continue
        if len(l)==0:
            return c+1
        temp=l.pop()
        if temp=='(' and i==')':
            c+=1
        elif temp=='[' and i==']':
            c+=1
        elif temp=='{' and i=='}':
            c+=1
        else:
            return c+1
    if len(l)==0:
        return 0
    else:
        return c+1
s=input()
print(demo(s))