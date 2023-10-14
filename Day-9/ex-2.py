'''
Take the input from the user in the given format(consist of name and code)
find the max digit from the code which is less or equal to the length of string and put the
place char in the final string, if there is no any digit found which not satisfy the condition
that simply put 'X'.
#input:
Abhishek:43848, Mayur:3749, Friend:3949, Yeah:7878
#output:kueX
'''

dict1 = {"Abhishek": 43848, "Mayur": 3749, "Yeah": 7878, "Friend": 3949}
result=""
for x, y in dict1.items():
    l1=[]
    y=str(y)
    for i in y:
        l1.append(int(i))
    while True:
        if(len(l1)==0):
            result+='X'
            break
        k=max(l1)
        #print(k)
        if(k<=len(x)):
            result+=x[(k-1)]
            #print(result)
            break
        else:
            l1.remove(k)
print(result)