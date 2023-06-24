#implementation of  single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                #temp.data means first node's data
                temp=temp.next #establishing link
obj1=singlelinkedlist()
#Node creation - initializing
n=Node(10) #so n.data in Node class will be 10
obj1.head=n #assigning first node as head
n1=Node(20)
obj1.head.next=n1 #nextnodevalue
n2=Node(30)
n1.next=n2
obj1.display()