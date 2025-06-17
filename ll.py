class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class linkedList:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode
    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=newNode
    def insertAtpos(self,data,index):
        if index==0:
            self.insertAtBegin(data)
            return
        else:
            pos=0
            temp=self.head
            while(temp.next!= None and pos+1 != index ):
                pos=pos+1
                temp=temp.next
            if pos+1==index:
                newNode=Node(data)
                newNode.next=temp.next
                temp.next=newNode
            else:
                print("index not found")
    def updateVal(self,val,index):
        temp=self.head
        pos=0
        if index==0:
            temp.data=val
        else:
            while(temp!=None and pos!= index):
                temp=temp.next
                pos=pos+1
            if pos==index:
                temp.data=val
            else:
                print("index not found")
    def delAtbegin(self):
        if self.head is None:
            return
        else:
            self.head=self.head.next
    def delAtEnd(self):
        if self.head is None:
            return
        else:
            temp=self.head
            while(temp.next!=None and temp.next.next!=None):
                temp=temp.next
            temp.next=None
    def delAtpos(self,index):
        if self.head is None:
            return
        if index==0:
            self.delAtbegin()
            return
        else:
            temp=self.head
            pos=0
            while(temp is not None and pos<index-1):
                pos=pos+1
                temp=temp.next
            if temp.next is None or temp is None:
                print("index not present ")
            else:
                temp.next=temp.next.next
    def delNode(self,data):
        if self.head.data==data:
            self.delAtbegin()
        else:
            temp=self.head
            while(temp!= None and temp.next.data!=data):
                temp=temp.next
            if temp is None:
                return
            else:
                temp.next=temp.next.next

    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def size(self):
        size=0
        if(self.head):
            temp=self.head
            while(temp):
                temp=temp.next
                size=size+1
            return size
        else:
            return 0

    def rev(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
ll=linkedList()
ll.insertAtBegin(10)
ll.insertAtBegin(12)
ll.insertAtEnd(14)
ll.insertAtEnd(55)
ll.insertAtpos(17,2)
print("sizde of linked list is : ", ll.size())
ll.print()
ll.rev()
ll.print()

