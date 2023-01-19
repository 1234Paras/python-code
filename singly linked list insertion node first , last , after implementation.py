'''program to implement singly linked list insert
the node first , last and after node in python.'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

llist = LinkedList()
llist.append(9)
llist.push(6)
llist.push(7)
llist.push(10)
llist.append(4)
llist.insertAfter(llist.head.next,8)
print("Created linked list is ")
llist.printlist()
