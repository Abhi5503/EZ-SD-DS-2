class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def display(self):
        if self.head is None:
            print("Circular List is empty!")
        else:
            temp=self.head
            while (temp.next!=self.head):
                print(temp.data,"->",end="")
                temp=temp.next
            print(temp.data,"->",end="")
            print(temp.next.data)

    def insert_beg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head
            
    def insert_pos(self,pos,data):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
        self.tail.next=self.head

    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while (temp.next!=self.head):
            temp=temp.next
            prev=prev.next
        temp.next=None
        self.tail=prev
        self.tail.next=self.head

    def delete_pos(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
     
node_1=Node(5)
node_2=Node(10)

cl=CLL()

cl.head=node_1
node_1.next=node_2

node_3=Node(15)
node_2.next=node_3

node_4=Node(20)
node_3.next=node_4

node_5=Node(25)
node_4.next=node_5

node_6=Node(30)
node_5.next=node_6

cl.tail=node_6
cl.tail.next=cl.head

'''
print(cl.tail.next.data)
print(node_1.next.data)
print(node_2.next.data)
print(node_3.next.data)
print(node_4.next.data)
print(node_5.next.data)
print(node_6.next.data)
'''

print("Display all the elements of circular linked list...")
cl.display()
print("Insert at beginning...")
cl.insert_beg(6)
cl.display()
print("Insert at end.....")
cl.insert_end(8)
cl.display()
print("Insert at position 3...")
cl.insert_pos(3,"bye")
cl.display()
print("Delete at beginning....")
cl.delete_beg()
cl.display()
print("Delete at end...")
cl.delete_end()
cl.display()
print("Delete at position 2....")
cl.delete_pos(2)
cl.display()

'''
print(node_1)
print(node_2)
print(node_3)
'''
