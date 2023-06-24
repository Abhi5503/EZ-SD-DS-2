stc=[]
def push_element():
    if len(stc)==n:
        print("Stack is full!")
    else:
        element=input("Enter element into stack:")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("Stack is empty!add element to continue..")
    else:
        element=stc.pop()
        print(element,"is deleted from the stack")
        print(stc)
n=int(input("Enter the size of stack"))
while True:
    print("Select the operation...1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("XXXXEnter the right operation you guddi idiot!!XXX")