class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAtPos(self, data, index):
        if index == 0:
            self.insertAtBegin(data)
            return
        newNode = Node(data)
        temp = self.head
        pos = 0
        while temp and pos < index - 1:
            temp = temp.next
            pos += 1
        if temp is None:
            print("Index out of range.")
            return
        newNode.next = temp.next
        newNode.prev = temp
        if temp.next:
            temp.next.prev = newNode
        temp.next = newNode

    def deleteAtBegin(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteAtEnd(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None  # Only one element

    def deleteAtPos(self, index):
        if self.head is None:
            return
        if index == 0:
            self.deleteAtBegin()
            return
        temp = self.head
        pos = 0
        while temp and pos < index:
            temp = temp.next
            pos += 1
        if temp is None:
            print("Index not found.")
            return
        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def updateAtPos(self, data, index):
        temp = self.head
        pos = 0
        while temp and pos < index:
            temp = temp.next
            pos += 1
        if temp:
            temp.data = data
        else:
            print("Index not found.")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def reverse(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def displayForward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.next
        print("None")

    def displayBackward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("None")
