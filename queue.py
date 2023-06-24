queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full!")
    else:
        ele=input("enter the element for queue:")
        queue.append(ele)
        print(queue)
def dequeue():
    if not queue:
        print("Queue is empty!")
    else:
        ele=queue.pop(0)
        print(ele,"is removed")
        print(queue)
n=int(input("Enter the size of queue"))
while True:
    print("Select the operation 1.enqueue 2.dequeue 3.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("XXX!!Enter the right operation!!XXX")